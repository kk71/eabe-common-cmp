import settings
settings.BackendConf.init()

from settings import *
CONFIG = {
    "connections": {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': backend_conf.mysql_host,
                'port': backend_conf.mysql_port,
                'user': backend_conf.mysql_user,
                'password': backend_conf.mysql_password,
                'database': backend_conf.mysql_db,
            }
        }
    },
    "apps": {
        'models': {
            'models': ["backend.models"],
            "default_connection": "default",
        },
    },
    "use_tz": False,
    "timezone": "UTC",
}

def tortoise_sync(coroutine):
    """不得已情况下的阻塞式tortoise方法处理器"""
    from tortoise import run_async, Tortoise
    async def inner():
        await Tortoise.init(config=CONFIG)
        return await coroutine
    run_async(inner())

del backend_conf


from .base import *
from .celery_task import *
from .user import *
from .role import *
from .user_role import *
from .cart import *
from .product import *
from .month_bill import *
from .order import *
from .wallet import *
