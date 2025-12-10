__all__ = [
    "app"
]

import settings
settings.BackendConf.init()
from settings import backend_conf

from tortoise import Tortoise
Tortoise.init_models(["backend.models"], "models")

from backend.celery import conf
from celery import current_app
current_app.config_from_object(conf)
from backend.core.import_utils import *
recursively_import_packages("backend.services")

from fastapi import FastAPI
from backend.apis import router
from backend.core.http import HttpError
app = FastAPI(
    title="Eabe Common CMP",
    exception_handlers={Exception: HttpError.exception_handler},
    root_path="/api" if backend_conf.prod_env else ""
)
recursively_import_packages("backend.apis")
app.include_router(router)

from tortoise.contrib.fastapi import register_tortoise
from backend import models
register_tortoise(app=app, config=models.CONFIG)
