from typing import Annotated, Any

from fastapi import Header
from pydantic import BaseModel, Field
from decimal import Decimal

from backend.core.tpdm import *
from backend.apis import *
from backend.models import *
from backend.apis.auth.base import *


@init_t_pdm
class MonthBillGetter(TGetter):
    class TMeta:
        cls = MonthBill


class MonthBillItem(BaseModel):
    """账单明细条目（来自月度账单记录）"""
    year: int
    month: int
    product_name: str | None
    customer_code: str
    customer_name: str
    account_code: str
    product_type: str
    resource_code: str | None
    amount: int | None
    settlement_type: str
    homepage_price: float
    discount_price: float
    total_paid: float


class MonthBillSummary(BaseModel):
    """按客户+月份汇总后的账单"""
    year: int
    month: int
    customer_code: str
    customer_name: str
    rent_amount: float = Field(description="月租费汇总")
    token_amount: float = Field(description="Token 使用费汇总")
    other_amount: float = Field(description="其他一次性费用汇总")
    total_amount: float = Field(description="当月总费用")
    items: list[MonthBillItem] = Field(default_factory=list, description="账单明细记录")


def classify_fee_type(bill: MonthBill) -> str:
    """与管理侧保持一致的费用分类规则"""
    pt = bill.product_type
    if pt in (ProductType.stream.value, ProductType.sms.value):
        return "token"
    if pt in (
        ProductType.ecs.value,
        ProductType.gpu.value,
        ProductType.bare_metal.value,
        ProductType.cloud_computer.value,
    ):
        return "rent"
    return "other"


@router.get(tags=[APITags.buyer], summary="查月账单明细（原始记录）")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "product_type": opt_query(ProductType.str_enum()),
            "settlement_type": opt_query(MonthBillSettlementType.str_enum()),
        }, pagination=True, keyword=True)
) -> PaginationJsonResp[list[MonthBillGetter]]:
    await header.verify()
    bills = MonthBill.filter(**query.model_dump())
    bills = query.query_keyword(
        bills, "product_name", "customer_name", "customer_code", "account_code", "resource_code")
    bills = await query.paginate(bills)
    return PaginationJsonResp(
        data=[await MonthBillGetter.parse_record(i) for i in bills],
        pagination=query.pagination
    )


@router.get(tags=[APITags.buyer], summary="查月账单汇总（按月一张账单）", path="/sell/bill/month/summary")
async def month_bill_summary(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "year": opt_query(int),
            "month": opt_query(int),
        }, keyword=False)
) -> JsonResp[list[MonthBillSummary]]:
    """
    为客户侧提供“每月一张账单”的视图，
    并按【月租费 / Token 使用费 / 其他一次性费用】拆分金额。
    """
    await header.verify()
    filters = query.model_dump()
    bills_qs = MonthBill.filter(**{k: v for k, v in filters.items() if v is not None})
    bills = await bills_qs

    grouped: dict[tuple[int, int, str], MonthBillSummary] = {}

    for b in bills:
        key = (b.year, b.month, b.customer_code)
        if key not in grouped:
            grouped[key] = MonthBillSummary(
                year=b.year,
                month=b.month,
                customer_code=b.customer_code,
                customer_name=b.customer_name,
                rent_amount=0.0,
                token_amount=0.0,
                other_amount=0.0,
                total_amount=0.0,
                items=[],
            )
        summary = grouped[key]

        fee_type = classify_fee_type(b)
        amount = float(Decimal(b.total_paid))
        if fee_type == "rent":
            summary.rent_amount += amount
        elif fee_type == "token":
            summary.token_amount += amount
        else:
            summary.other_amount += amount
        summary.total_amount += amount

        summary.items.append(
            MonthBillItem(
                year=b.year,
                month=b.month,
                product_name=b.product_name,
                customer_code=b.customer_code,
                customer_name=b.customer_name,
                account_code=b.account_code,
                product_type=b.product_type,
                resource_code=b.resource_code,
                amount=b.amount,
                settlement_type=b.settlement_type,
                homepage_price=float(b.homepage_price),
                discount_price=float(b.discount_price),
                total_paid=float(b.total_paid),
            )
        )

    results = sorted(grouped.values(), key=lambda x: (x.year, x.month, x.customer_code), reverse=True)
    return JsonResp(data=results)

