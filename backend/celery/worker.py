import settings
settings.BackendConf.init()

from backend.core.import_utils import *
from . import conf
from celery import current_app
recursively_import_packages("backend.services")
recursively_import_packages("backend.celery.tasks")
current_app.config_from_object(conf)

# TODO the import sentences should be reserved for celery worker!
