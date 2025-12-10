from typing import Annotated, Any

from fastapi import Header

from backend.core.tpdm import *
from backend.apis import *
from backend.models import *
from backend.apis.auth.base import *


@init_t_pdm
class CeleryTaskRecordGetter(TGetter):
    class TMeta:
        cls = CeleryTaskRecord


@router.get(tags=[APITags.system], summary="查询异步任务")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "id": opt_query(int),
            "status": opt_query(CeleryTaskStatus.str_enum()),
        }, keyword=True, pagination=True)
) -> PaginationJsonResp[list[CeleryTaskRecordGetter]]:
    await header.verify()
    q = CeleryTaskRecord.filter(**query.model_dump())
    q = query.query_keyword(q, "task_description", "input", "output", "error_info")
    r = await query.paginate(q)
    return PaginationJsonResp(
        data=[await CeleryTaskRecordGetter.parse_record(i) for i in r],
        pagination=query.pagination
    )
