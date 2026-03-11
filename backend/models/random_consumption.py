__all__ = [
    "RandomConsumptionRule",
]

from decimal import Decimal

from tortoise.fields import BooleanField, CharField, DecimalField, IntField, TextField

from .base import *
from .product import ProductType


class RandomConsumptionRule(SoftDeletionModelMixin, BaseTModel):
    """随机生成消费流水的规则（用于 token/短信/流量等模拟消费）"""

    enabled = BooleanField(default=True, description="是否启用")

    customer_code = CharField(max_length=64, description="客户编码（对应钱包 customer_code）")
    customer_name = CharField(max_length=64, null=True, description="客户名称（可选）")

    product_type = ProductType.build_char_enum_field(max_length=64)
    min_amount = DecimalField(max_digits=16, decimal_places=2, default=Decimal("0.00"), description="最小扣费金额")
    max_amount = DecimalField(max_digits=16, decimal_places=2, default=Decimal("0.00"), description="最大扣费金额")

    # 每 N 分钟最多生成一条（简单限频，便于追溯/控制量）
    interval_minutes = IntField(default=60, description="生成间隔（分钟）")
    remark = TextField(null=True, description="备注/规则说明")

    Meta = build_soft_deletion_meta(
        table="random_consumption_rule",
        description="随机消费生成规则",
        ordering=("-create_time",),
    )

