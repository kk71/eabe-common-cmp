from typing import Annotated

from fastapi import Header

from backend.core.tpdm import *
from backend.apis import *
from backend.models import MonthBillChargeRecord, MonthBillChargeStatus
from backend.apis.auth.base import *


@init_t_pdm
class MonthBillChargeRecordGetter(TGetter):
    class TMeta:
        cls = MonthBillChargeRecord


@router.get(tags=[APITags.console], summary="查询月账单扣费记录")
async def _(
    header: Annotated[HeaderToken, Header()],
    query: build_query(
        {
            "year": opt_query(int),
            "month": opt_query(int),
            "customer_code": opt_query(str),
            "status": opt_query(MonthBillChargeStatus.str_enum()),
        },
        pagination=True,
        keyword=True,
    ),
) -> PaginationJsonResp[list[MonthBillChargeRecordGetter]]:
    await header.verify(Privileges.system_control)
    records = MonthBillChargeRecord.filter(**query.model_dump())
    records = query.query_keyword(records, "customer_code", "customer_name", "bill_key", "error_info")
    records = await query.paginate(records)
    return PaginationJsonResp(
        data=[await MonthBillChargeRecordGetter.parse_record(i) for i in records],
        pagination=query.pagination,
    )

