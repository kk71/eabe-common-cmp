__all__ = []

import time
import random
import inspect

from loguru import logger
from tqdm import tqdm


def random_sleep(min_sec: int, max_sec: int):
    """随机在给定的秒钟区间内执行sleep"""
    time.sleep(random.uniform(min_sec, max_sec))


def keep_trying(max_tries: int, desc: str = None, interval: int | tuple[int, int] = 1):
    """
    按照一定的时间间隔，不停尝试，直到达到最大次数
    :param max_tries: 最大次数
    :param desc: 本次循环是为了做什么。这段文本展示在日志以提示
    :param interval: 间隔秒数，或者指定随机秒数区间
    :return:
    """
    callee_stack = inspect.stack()[1]
    if desc:
        logger.info(desc)
    for i in tqdm(range(max_tries)):
        if isinstance(interval, int):
            time.sleep(interval)
        elif isinstance(interval, tuple):
            random_sleep(*interval)
        yield i
