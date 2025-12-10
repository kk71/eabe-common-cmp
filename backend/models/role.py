__all__ = [
    "Role",
]

from tortoise.fields import CharField, JSONField

from backend.core.soft_deletion import *
from .base import *


class Role(SoftDeletionModelMixin, BaseTModel):
    """角色"""
    name = CharField(max_length=32, description="角色名称")
    privileges = JSONField(field_type=list[str], null=True, description="角色拥有权限名")

    Meta = build_soft_deletion_meta(
        table="role",
        description="角色",
        unique_together=(("existed", "name"),)
    )
