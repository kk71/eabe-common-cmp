from typing import Annotated
from datetime import datetime
from decimal import Decimal

from fastapi import Header
from pydantic import BaseModel, Field

from backend.apis import *
from backend.apis.auth.base import *
from backend.core.tpdm import *
from backend.models import *
from backend.apis.sell.auth import verify_sell_user


class MonthAmountPoint(BaseModel):
    year: int
    month: int
    period: str = Field(description="YYYY-MM")
    amount: float = Field(description="当月总费用")


def _iter_recent_months(months: int) -> list[tuple[int, int]]:
    months = max(1, min(int(months), 36))
    now = datetime.now()
    y, m = now.year, now.month
    result: list[tuple[int, int]] = []
    for i in range(months - 1, -1, -1):
        mm = m - i
        yy = y
        while mm <= 0:
            mm += 12
            yy -= 1
        result.append((yy, mm))
    return result


@router.get(tags=[APITags.buyer], summary="成本/费用趋势（按月）")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "months": opt_query(int, default=6, description="最近N个月"),
            "customer_code": opt_query(str, description="客户编码（可选）"),
        }, keyword=False)
) -> JsonResp[list[MonthAmountPoint]]:
    await verify_sell_user(header)

    months = query.months or 6
    ym_list = _iter_recent_months(months)
    min_year = min(y for y, _ in ym_list)

    qs = MonthBill.filter(year__gte=min_year)
    if query.customer_code:
        qs = qs.filter(customer_code=query.customer_code)

    bills = await qs
    sums: dict[tuple[int, int], Decimal] = {(y, m): Decimal("0") for (y, m) in ym_list}
    for b in bills:
        key = (b.year, b.month)
        if key not in sums:
            continue
        sums[key] += Decimal(b.total_paid)

    points = [
        MonthAmountPoint(
            year=y,
            month=m,
            period=f"{y}-{str(m).zfill(2)}",
            amount=float(sums[(y, m)]),
        )
        for (y, m) in ym_list
    ]
    return JsonResp(data=points)

