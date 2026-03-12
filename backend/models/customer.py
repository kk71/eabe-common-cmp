__all__ = [
    "Customer",
]

from tortoise.fields import CharField, TextField

from .base import *


class Customer(SoftDeletionModelMixin, BaseTModel):
    """客户"""

    code = CharField(max_length=64, null=True, db_index=True, description="客户编号（导入唯一标识）")
    name = CharField(max_length=64, db_index=True, description="客户名")
    contact_phone = CharField(max_length=32, null=True, description="联系电话")
    principal = CharField(max_length=64, null=True, description="主要负责人")
    remark = TextField(null=True, description="备注")

    Meta = build_soft_deletion_meta(
        table="customer",
        description="客户表",
        unique_together=(("existed", "name"), ("existed", "code")),
    )

