__all__ = [
    "Order",
    "OrderOrigin",
    "OrderStatus",
]

import uuid

from tortoise.fields import IntField, TextField, CharField, DateField, DecimalField

from backend.core.status_machine import *
from .base import *
from .product import *


class OrderOrigin(StatusMachine):
    """订单区域"""
    EXPORT_FLAG = "order-origin"
    east_china_zhejiang = SMV("华东-浙江")
    south_china_guangzhou = SMV("华南-广州")


class OrderStatus(StatusMachine):
    """订单状态"""
    EXPORT_FLAG = "order-status"
    processing = SMV("进行中")
    paid = SMV("已支付")
    pay_failed = SMV("支付失败")


class Order(SoftDeletionModelMixin, BaseTModel):
    """订单"""
    order_id = CharField(max_length=64, default=lambda: uuid.uuid4().hex, editable=False, description="订单编号")
    batch_code = CharField(max_length=64, null=True, description="批次")
    product_name = TextField(null=True, description="产品名")
    resource_code = TextField(null=True, description="资源编号")
    order_guanxi_id = CharField(max_length=64, description="订购关系ID")
    origin = OrderOrigin.build_char_enum_field(max_length=64)
    product_type = ProductType.build_char_enum_field(max_length=64)
    order_date = DateField(null=True, db_index=True, description="下单时间")
    status = OrderStatus.build_char_enum_field(max_length=32)
    total_price = DecimalField(max_digits=10, decimal_places=2, default=0.00, description="总价")

    Meta = build_soft_deletion_meta(
        table="order",
        description="订单",
        ordering=("-order_date",)
    )
