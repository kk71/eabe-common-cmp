__all__ = [
    "MonthBillChargeRecord",
    "MonthBillChargeStatus",
]

from decimal import Decimal

from tortoise.fields import CharField, IntField, DecimalField, TextField

from backend.core.status_machine import *
from .base import *


class MonthBillChargeStatus(StatusMachine):
    """月账单扣费状态"""
    EXPORT_FLAG = "month-bill-charge-status"
    pending = SMV("待扣费")
    charged = SMV("已扣费")
    failed = SMV("扣费失败")


class MonthBillChargeRecord(SoftDeletionModelMixin, BaseTModel):
    """
    月账单汇总扣费记录（按 客户 + 年月 一次扣费）。
    用于保证幂等：同一个客户同一个年月只会生成/执行一次扣费。
    """

    year = IntField()
    month = IntField()
    customer_code = CharField(max_length=64, description="客户编码")
    customer_name = CharField(max_length=64, null=True, description="客户名称")

    bill_key = CharField(max_length=128, unique=True, description="幂等键：YYYYMM:customer_code")
    total_amount = DecimalField(max_digits=16, decimal_places=2, default=Decimal("0.00"), description="当月总金额")
    status = MonthBillChargeStatus.build_char_enum_field(max_length=32)

    related_bill_id = CharField(max_length=64, null=True, description="写入钱包流水的 related_bill_id")
    wallet_tx_id = CharField(max_length=64, null=True, description="关联钱包流水 tx_id（如有）")
    error_info = TextField(null=True, description="失败原因")

    Meta = build_soft_deletion_meta(
        table="month_bill_charge_record",
        description="月账单汇总扣费记录",
        ordering=("-create_time",),
        unique_together=(("year", "month", "customer_code"),),
    )

