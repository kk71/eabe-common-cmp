from enum import StrEnum

from backend.core.http import *

router = CollectAPIRouter(entry_module="backend.apis")


class APITags(StrEnum):
    """接口标签枚举"""
    sm = "状态机"
    source = "数据源"
    system = "系统"
    auth = "权限"
    buyer = "消费者"
    console = "管理后台"
