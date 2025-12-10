__all__ = [
    "Cart",
]

from tortoise.fields import JSONField

from .base import *
from .product import *


class Cart(SoftDeletionModelMixin, BaseTModel):
    """购物车"""
    user = EasyForeignKeyField("models.User", related_name="carts")
    detail = JSONField(field_type=list[Product], default=list, null=True)

    Meta = build_soft_deletion_meta(
        table="cart",
        description="购物车",
    )
