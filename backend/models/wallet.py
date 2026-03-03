__all__ = [
    "WalletAccount",
    "WalletTransaction",
    "WalletTransactionType",
]

import uuid

from decimal import Decimal
from tortoise.fields import CharField, DecimalField, TextField

from backend.core.status_machine import *
from .base import *


def generate_tx_id() -> str:
    return uuid.uuid4().hex


class WalletTransactionType(StatusMachine):
    """钱包流水类型"""
    EXPORT_FLAG = "wallet-transaction-type"
    recharge = SMV("充值")
    consume = SMV("消费")
    refund = SMV("退款")
    adjust = SMV("调整")


class WalletAccount(SoftDeletionModelMixin, BaseTModel):
    """预充值钱包账户（按客户维度）"""
    customer_code = CharField(max_length=64, unique=True, description="客户编码")
    customer_name = CharField(max_length=64, null=True, description="客户名称")
    balance = DecimalField(max_digits=16, decimal_places=2, default=Decimal("0.00"), description="可用余额")
    frozen_balance = DecimalField(max_digits=16, decimal_places=2, default=Decimal("0.00"), description="冻结余额")
    total_recharge = DecimalField(max_digits=16, decimal_places=2, default=Decimal("0.00"), description="累计充值金额")
    currency = CharField(max_length=16, default="CNY", description="币种")

    Meta = build_soft_deletion_meta(
        table="wallet_account",
        description="预充值钱包账户",
        ordering=("-create_time",),
    )


class WalletTransaction(SoftDeletionModelMixin, BaseTModel):
    """钱包账户流水"""
    tx_id = CharField(max_length=64, default=generate_tx_id, description="流水编号")
    wallet = EasyForeignKeyField("models.WalletAccount", related_name="transactions", description="关联钱包账户")
    tx_type = WalletTransactionType.build_char_enum_field(max_length=64)
    change_amount = DecimalField(max_digits=16, decimal_places=2, description="变动金额，正为入账，负为出账")
    balance_after = DecimalField(max_digits=16, decimal_places=2, description="变动后的可用余额")
    related_order_id = CharField(max_length=64, null=True, description="关联订单编号")
    related_bill_id = CharField(max_length=64, null=True, description="关联账单ID或编号")
    remark = TextField(null=True, description="备注")

    Meta = build_soft_deletion_meta(
        table="wallet_transaction",
        description="钱包账户流水",
        ordering=("-create_time",),
    )

