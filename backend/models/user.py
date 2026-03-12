__all__ = [
    "User",
]

import uuid

from tortoise.fields import TextField, CharField, BooleanField

from .base import *


def generate_user_id() -> str:
    return uuid.uuid4().hex


class User(SoftDeletionModelMixin, BaseTModel):
    """用户"""
    id = CharField(primary_key=True, default=generate_user_id, max_length=64, description="用户唯一id")
    name = CharField(max_length=32)
    avatar = TextField(null=True)
    email = TextField(null=True, description="邮箱")
    is_admin = BooleanField(default=False, db_index=True, description="是否为最高权限拥有者")
    disabled = BooleanField(default=False, db_index=True, description="是否禁用")
    login_name = CharField(max_length=32, null=True, db_index=True, description="用于密码登录的用户名")
    password = TextField(null=True, description="密码密文")
    douyin_unique_id = CharField(max_length=32, null=True, description="抖音号（见个人页面）")
    customer = EasyForeignKeyField("models.Customer", related_name="users", null=True, description="所属客户（仅非管理员用户可绑定）")

    Meta = build_soft_deletion_meta(
        table="user",
        description="用户表",
        unique_together=(("existed", "login_name"),)
    )
