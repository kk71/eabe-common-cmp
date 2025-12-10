from typing import Annotated, Any

from fastapi import Header

from backend.core.tpdm import *
from backend.apis import *
from backend.models import *
from backend.apis.auth.base import *


@init_t_pdm
class MonthBillGetter(TGetter):
    class TMeta:
        cls = MonthBill


@router.get(tags=[APITags.buyer], summary="查月账单")
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
