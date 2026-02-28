from typing import Annotated

from fastapi import Header
from pydantic import BaseModel, Field
from decimal import Decimal

from backend.core.tpdm import *
from backend.apis import *
from backend.models import *
from backend.services.auth import *
from backend.apis.auth.base import *


class PaymentStats(BaseModel):
    """订单支付统计"""
    paid_amount: float = Field(description="已支付订单总金额")
    paid_count: int = Field(description="已支付订单数量")
    failed_amount: float = Field(description="支付失败订单总金额")
    failed_count: int = Field(description="支付失败订单数量")
    processing_amount: float = Field(description="待支付订单总金额")
    processing_count: int = Field(description="待支付订单数量")


@router.get(tags=[APITags.console], summary="订单支付统计")
async def _(
        header: Annotated[HeaderToken, Header()],
) -> JsonResp[PaymentStats]:
    await header.verify(Privileges.system_control)

    paid_orders = await Order.filter(status=OrderStatus.paid.value)
    failed_orders = await Order.filter(status=OrderStatus.pay_failed.value)
    processing_orders = await Order.filter(status=OrderStatus.processing.value)

    def sum_amount(os):
        total = Decimal("0")
        for o in os:
            total += Decimal(o.total_price)
        return float(total)

    stats = PaymentStats(
        paid_amount=sum_amount(paid_orders),
        paid_count=len(paid_orders),
        failed_amount=sum_amount(failed_orders),
        failed_count=len(failed_orders),
        processing_amount=sum_amount(processing_orders),
        processing_count=len(processing_orders),
    )
    return JsonResp(data=stats)

