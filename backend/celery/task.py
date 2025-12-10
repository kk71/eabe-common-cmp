# Author: kk.Fang(fkfkbill@gmail.com)

__all__ = [
    "ScheduledJobTrigger",
    "ScheduledJobTriggerArgsCron",
    "ScheduledJobTriggerArgsInterval",
    "BaseCeleryTask",
    "register_celery_task",
]

import pickle
import asyncio
import traceback
from typing import Type
from enum import StrEnum
from datetime import datetime

import chardet
from loguru import logger
from kombu import Exchange, Queue
from celery import current_app
from pydantic import BaseModel, ConfigDict

from backend.models import CeleryTaskRecord, CeleryTaskStatus, tortoise_sync
from utils import dt_utils
from . import conf as celery_conf


# 存放所有收集到的任务
all_tasks: list[Type["BaseCeleryTask"]] = []


def add_task(task_type: str, module_to_import: str):
    """增加任务"""
    if celery_conf is None:
        raise Exception("celery conf unset.")
    celery_conf.task_routes.update({
        task_type: {'queue': task_type, 'routing_key': task_type}
    })
    celery_conf.task_queues.add(
        Queue(task_type, Exchange(task_type), routing_key=task_type)
    )
    celery_conf.imports.append(module_to_import)


def register_celery_task(task_class: Type["BaseCeleryTask"]):
    """注册任务"""
    task_class.verify_scheduled_trigger()
    if not getattr(task_class, "name", None):
        task_class.name = getattr(task_class, "task_type", None)
    if not getattr(task_class, "name", None):
        # 如果name和task_type都未设定，那么使用类名作为类型名
        task_class.task_type = task_class.name = task_class.__name__

    add_task(task_class.task_type, task_class.__module__)
    current_app.register_task(task_class())
    task_class._task_instance = current_app.tasks[task_class.task_type]
    global all_tasks
    all_tasks.append(task_class)
    return task_class


class ScheduledJobTrigger(StrEnum):
    interval = "interval"
    cron = "cron"


class ScheduledJobTriggerArgsInterval(BaseModel):
    weeks: int | None = None
    days: int | None = None
    hours: int | None = None
    minutes: int | None = None
    seconds: int | None = None
    start_date: datetime | str | None = None
    end_date: datetime | str | None = None
    jitter: int | None = None


class DayOfWeek(StrEnum):
    mon = "mon"
    tue = "tue"
    wed = "wed"
    thu = "thu"
    fri = "fri"
    sat = "sat"
    sun = "sun"


class ScheduledJobTriggerArgsCron(BaseModel):
    year: int | str | None = None
    month: int | str | None = None
    day: int | str | None = None
    week: int | str | None = None
    day_of_week: int | DayOfWeek | None = None
    hour: int | str | None = None
    minute: int | str | None = None
    second: int | str | None = None
    start_date: datetime | str | None = None
    end_date: datetime | str | None = None


class BaseCeleryTask(current_app.Task):
    """基础celery任务"""

    # 任务类型
    name = task_type = None
    # name字段是celery预留的，task_type是项目字段
    # name用于celery标识任务的名称，本质就是task_type

    # 不写入日志
    NO_RECORD: bool = False

    # 不记录输入
    NO_INPUT: bool = False

    # 配置定时任务类型的参数，具体参考apscheduler.schedulers.base.add_job
    SCHEDULED_JOB_TRIGGER: ScheduledJobTrigger | None = None
    SCHEDULED_JOB_TRIGGER_ARGS: ScheduledJobTriggerArgsInterval | ScheduledJobTriggerArgsCron | None = None

    @classmethod
    def verify_scheduled_trigger(cls):
        if not cls.SCHEDULED_JOB_TRIGGER:
            return
        for i in ScheduledJobTrigger:
            if cls.SCHEDULED_JOB_TRIGGER == i.value:
                if i is ScheduledJobTrigger.interval:
                    assert isinstance(cls.SCHEDULED_JOB_TRIGGER_ARGS, ScheduledJobTriggerArgsInterval)
                elif i is ScheduledJobTrigger.cron:
                    assert isinstance(cls.SCHEDULED_JOB_TRIGGER_ARGS, ScheduledJobTriggerArgsCron)
                break
        else:
            raise ValueError(f"bad {cls.SCHEDULED_JOB_TRIGGER=}")

    def __str__(self):
        infos = list()
        infos.append(self.task_type)
        if self.SCHEDULED_JOB_TRIGGER:
            infos.append(f"scheduled as {self.SCHEDULED_JOB_TRIGGER} at {self.SCHEDULED_JOB_TRIGGER_ARGS}")
        return "celery-task(" + ", ".join(infos) + ")"

    def run(self, task_record_id: int, **kwargs):
        """
        :param task_record_id:
        :param kwargs:
        """
        '''
        # 用来解决找不到代码根目录的问题
        sys.path.append(settings.BASE_DIR)
        '''
        self.task_record_id = task_record_id
        logger.info(f"task {self.task_type}: {self.task_record_id}")
        if not self.NO_RECORD:
            async def runner():
                task_record = await CeleryTaskRecord.filter(id=self.task_record_id).first()
                if task_record:
                    task_record.status = CeleryTaskStatus.running.value
                    await task_record.save()
            tortoise_sync(runner())
        if asyncio.iscoroutinefunction(self.task):
            return tortoise_sync(self.task(task_record_id, **kwargs))
        else:
            return self.task(task_record_id, **kwargs)

    @classmethod
    def task(cls, task_record_id: int | None = None, **kwargs):
        """
        重写该方法以实现任务的实际功能
        TODO 该方法写成静态，是为了和celery脱离关系，
            使得必要时可以静态运行任务而不需要队列
        :param task_record_id:
        :param kwargs:
        """
        raise NotImplementedError

    def on_success(self, retval, task_id, args, kwargs):
        if not self.NO_RECORD:
            async def runner():
                task_record = await CeleryTaskRecord.filter(id=self.task_record_id).first()
                if task_record:
                    task_record.status = CeleryTaskStatus.done.value
                    task_record.end_time = dt_utils.dt_now()
                    task_record.output = pickle.dumps(retval, protocol=0).decode()
                    await task_record.save()
            tortoise_sync(runner())

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        failure_info = traceback.format_exc()
        logger.error(f"task {self.task_type} ({self.task_type}, task_record_id:{self.task_record_id}) just failed.")
        if not self.NO_RECORD:
            async def runner():
                task_record = await CeleryTaskRecord.filter(id=self.task_record_id).first()
                if task_record:
                    task_record.status = CeleryTaskStatus.failed.value
                    task_record.end_time = dt_utils.dt_now()
                    task_record.error_info = failure_info[-4999:]
                    await task_record.save()
            tortoise_sync(runner())

    @classmethod
    async def _shoot(cls, **kwargs) -> int | None:
        if not cls.NO_RECORD:
            pickled = pickle.dumps(kwargs, protocol=0)
            pickled_decoded = None
            if not cls.NO_INPUT:
                pickled_decoded = pickled.decode(chardet.detect(pickled)["encoding"])
            task_record = CeleryTaskRecord(
                task_type=cls.task_type,
                task_description=cls.__doc__,
                start_time=dt_utils.dt_now(),
                input=pickled_decoded
            )
            await task_record.save()
            return task_record.id

    @classmethod
    async def shoot(cls, **kwargs) -> int:
        """
        调用当前任务，不等待返回
        :param kwargs: 具体因具体任务决定
        :return: task_record_id
        """
        task_record_id = await cls._shoot(**kwargs)
        cls._task_instance.delay(task_record_id, **kwargs)
        return task_record_id
