__all__ = []

import arrow
from datetime import date, datetime, time

from .const import \
    COMMON_DATETIME_FORMAT, COMMON_DATE_FORMAT, COMMON_TIME_FORMAT, \
    COMMON_DATETIME_FORMAT_COMPACT, COMMON_DATE_FORMAT_COMPACT


def dt_now() -> datetime:
    """返回无时区的当前时间"""
    return arrow.utcnow().shift(hours=+8).datetime.replace(tzinfo=None)


def arrow_now() -> arrow.Arrow:
    """返回无时区的当前时间arrow"""
    return arrow.get(dt_now())


def dt_to_str(
        dt: datetime |arrow.Arrow | list | tuple | dict,
        fmt=COMMON_DATETIME_FORMAT) -> str | list | dict:
    if isinstance(dt, (datetime, arrow.Arrow)):
        return arrow.get(dt).format(fmt=fmt)

    elif isinstance(dt, (list, tuple)):
        return [dt_to_str(i) for i in dt]

    elif isinstance(dt, dict):
        return {k: dt_to_str(v) for k, v in dt.items()}

    else:
        return dt


def d_to_str(
        d: datetime | arrow.Arrow | date | list | tuple | dict,
        fmt=COMMON_DATE_FORMAT) -> str | list | dict:
    if isinstance(d, (date, arrow.Arrow)):
        return arrow.get(d).format(fmt=fmt)

    elif isinstance(d, (list, tuple)):
        return [d_to_str(i) for i in d]

    elif isinstance(d, dict):
        return {k: d_to_str(v) for k, v in d.items()}

    else:
        return d


def t_to_str(t: time, fmt=COMMON_TIME_FORMAT) -> str | None:
    if not t:
        return None
    return arrow.now().replace(
        hour=t.hour, minute=t.minute, second=t.second).format(fmt=fmt)


def str_to_dt(
        s: str,
        allow_none_to_none: bool = True) -> datetime | None:
    if s is None and allow_none_to_none:
        return None
    return arrow.get(s).datetime.replace(tzinfo=None)


def str_to_d(
        s: str,
        allow_none_to_none: bool = True) -> date | None:
    if s is None and allow_none_to_none:
        return None
    return arrow.get(s).date()


def str_to_t(
        s: str,
        allow_none_to_none: bool = True,
        fmt=COMMON_TIME_FORMAT) -> time | None:
    if s is None and allow_none_to_none:
        return None
    return arrow.get(s, [fmt]).time()
