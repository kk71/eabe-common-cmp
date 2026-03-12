from typing import Annotated, Any

from fastapi import Header

from backend.core.tpdm import *
from backend.apis import *
from backend.models import *
from backend.services.auth import *
from backend.apis.auth.base import *
from backend.apis.sell.auth import verify_sell_user


@init_t_pdm
class OrderGetter(TGetter):
    class TMeta:
        cls = Order


@router.get(tags=[APITags.buyer], summary="查询订单")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "id": opt_query(int),
            "order_id": opt_query(str),
            "product_type": opt_query(ProductType.str_enum()),
            "status": opt_query(OrderStatus.str_enum()),
            "origin": opt_query(OrderOrigin.str_enum()),
        }, pagination=True, keyword=True)
) -> PaginationJsonResp[list[OrderGetter]]:
    await verify_sell_user(header)
    orders = Order.filter(**query.model_dump())
    orders = query.query_keyword(orders, "order_id", "batch_code", "product_name", "resource_code")
    orders = await query.paginate(orders)
    return PaginationJsonResp(
        data=[await OrderGetter.parse_record(i) for i in orders],
        pagination=query.pagination
    )
