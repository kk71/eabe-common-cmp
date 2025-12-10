__all__ = [
    "asyncio_run",
]

import asyncio
import functools


def asyncio_run(func):
    """装饰一个async方法在无loop的线程中同步执行"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return asyncio.run(func(*args, **kwargs))
    return wrapper