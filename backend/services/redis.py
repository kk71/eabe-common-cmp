__all__ = [
    "redis_cli",
    "root_template",
]

from redis.asyncio import Redis

from settings import backend_conf
from backend.core.redis_key import *


def get_redis() -> Redis:
    return Redis(
        host=backend_conf.redis_host,
        port=backend_conf.redis_port,
        username=backend_conf.redis_user,
        password=backend_conf.redis_password,
        db=backend_conf.redis_db
    )

# 全局实例
redis_cli = get_redis()

# 全局根模板
root_template = RedisKeyTemplate.build("live")
