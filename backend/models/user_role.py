__all__ = [
    "UserRole",
]

from .base import *


class UserRole(BaseTModel):
    """用户角色关系表"""
    user = EasyForeignKeyField("models.User", related_name="user_roles")
    role = EasyForeignKeyField("models.Role", related_name="role_users")

    Meta = build_meta(
        table="user_role",
        description="用户角色关系"
    )
