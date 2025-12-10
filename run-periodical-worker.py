#!/usr/bin/env python3
import settings
settings.BackendConf.init()

import asyncio
from loguru import logger
from rich import print
from apscheduler.schedulers.blocking import BlockingScheduler
from tortoise import Tortoise, connections

from backend.celery import BaseCeleryTask
from backend.core.import_utils import *
recursively_import_packages("backend.services")
from backend.celery.task import all_tasks
from celery import current_app
from backend.celery import conf
current_app.config_from_object(conf)
from backend.models import CONFIG


def run(task_obj: BaseCeleryTask):
    logger.info(f"running {task_obj} ...")
    async def inner():
        await Tortoise.init(
            config=CONFIG,
        )
        await Tortoise.generate_schemas()
        try:
            await task_obj.shoot()
        finally:
            await connections.close_all(discard=True)
    asyncio.run(inner())


def main():
    scheduler = BlockingScheduler()
    for ti in all_tasks:
        if ti.SCHEDULED_JOB_TRIGGER:
            print(f"watching: {ti} ...")
            scheduler.add_job(
                lambda: run(ti),
                trigger=str(ti.SCHEDULED_JOB_TRIGGER),
                **ti.SCHEDULED_JOB_TRIGGER_ARGS.model_dump(exclude_none=True)
            )
    scheduler.start()


if __name__ == "__main__":
    main()
