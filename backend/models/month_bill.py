__all__ = [
    "MonthBill",
    "MonthBillSettlementType",
]

from tortoise.fields import IntField, TextField, CharField, DecimalField

from backend.core.status_machine import *
from .product import *
from .base import *


class MonthBillSettlementType(StatusMachine):
    """账单的出账类型"""
    EXPORT_FLAG = "bill-settlement-type"
    consumption_settle = SMV("消费出账")


class MonthBill(SoftDeletionModelMixin, BaseTModel):
    """月度账单"""
    year = IntField()
    month = IntField()
    product_name = TextField(null=True, description="商品名")
    customer_code = CharField(max_length=64, description="客户编码")
    customer_name = CharField(max_length=64, description="客户名称")
    account_code = CharField(max_length=64, description="订购账号名")
    product_type = ProductType.build_char_enum_field(max_length=64)
    resource_code = TextField(null=True, description="资源编号")
    amount = IntField(default=0, null=True, description="用量")
    settlement_type = MonthBillSettlementType.build_char_enum_field(max_length=64)
    homepage_price = DecimalField(max_digits=10, decimal_places=2, default=0.00, description="官网价")
    discount_price = DecimalField(max_digits=10, decimal_places=2, default=0.00, description="优惠价格")
    total_paid = DecimalField(max_digits=10, decimal_places=2, default=0.00, description="实付金额")

    Meta = build_soft_deletion_meta(
        table="month_bill",
        description="月度账单",
        ordering=("-year", "-month"),
    )
