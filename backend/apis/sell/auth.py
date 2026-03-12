from __future__ import annotations

from backend.apis.auth.base import HeaderToken
from backend.core.http import Forbidden


async def verify_sell_user(header: HeaderToken, *any_privileges) -> None:
    """
    客户侧（sell）接口统一鉴权：
    - 必须已登录（token有效）
    - 管理员不属于客户，禁止进入客户侧管理后台
    """
    await header.verify(*any_privileges)
    if header.user.is_admin:
        raise Forbidden("管理员禁止进入客户侧管理后台")

