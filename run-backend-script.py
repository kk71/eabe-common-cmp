#!/usr/bin/env python3
import importlib
from sys import argv

from loguru import logger
from rich import print

from backend.app import *
from backend.models import tortoise_sync

module_name = f"backend.{argv[1]}"
module = importlib.import_module(module_name)
runner = getattr(module, "script", None)
if not runner:
    raise NotImplementedError(f"module {module_name} contains no async function named 'script'")
logger.info(f"running {module_name}::script() ...\n")
ret = tortoise_sync(runner())
