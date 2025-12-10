__all__ = [
    "CeleryTaskStatus",
    "CeleryTaskRecord",
]

from tortoise import fields

from backend.core.status_machine import *
from .base import *


class CeleryTaskStatus(StatusMachine):
    """celery任务的状态"""
    EXPORT_FLAG = "celery-task-status"
    never_ran = SMV("未执行", extra={"tag_type": "info"})
    pending = SMV("待执行", extra={"tag_type": "info"})
    running = SMV("执行中", extra={"tag_type": "warning"})
    done = SMV("成功", extra={"tag_type": "success"})
    failed = SMV("失败", extra={"tag_type": "danger"})


class CeleryTaskRecord(BaseTModel):
    """基础的celery任务执行记录表"""
    task_type = fields.CharField(max_length=128, db_index=True, help_text=f"任务类名")
    task_description = fields.TextField(null=True, help_text="描述")
    start_time = fields.DatetimeField(null=True, help_text="开始时间")
    end_time = fields.DatetimeField(null=True, help_text="结束时间")
    status = CeleryTaskStatus.build_char_enum_field(max_length=16, default=CeleryTaskStatus.pending.value)
    input = fields.TextField(null=True, help_text="输入pickle")
    output = fields.TextField(null=True, help_text="输出pickle")
    error_info = fields.TextField(null=True, help_text="报错信息")

    Meta = build_meta(
        table="celery_task_record",
        table_description="celery任务日志表",
    )
