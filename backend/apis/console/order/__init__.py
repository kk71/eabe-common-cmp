from typing import Annotated, Any

from fastapi import Header

from backend.core.tpdm import *
from backend.apis import *
from backend.models import *
from backend.services.auth import *
from backend.services import WalletAccountService
from backend.core.http import Forbidden
from backend.apis.auth.base import *


@init_t_pdm
class OrderGetter(TGetter):
    class TMeta:
        cls = Order


@router.get(tags=[APITags.console], summary="查询订单")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "id": opt_query(int),
            "order_id": opt_query(str),
            "origin": opt_query(OrderOrigin.str_enum()),
            "product_type": opt_query(ProductType.str_enum()),
            "status": opt_query(OrderStatus.str_enum()),
        }, pagination=True, keyword=True)
) -> PaginationJsonResp[list[OrderGetter]]:
    await header.verify(Privileges.system_control)
    orders = Order.filter(**query.model_dump())
    orders = query.query_keyword(orders, "order_id", "batch_code", "product_name", "resource_code")
    orders = await query.paginate(orders)
    return PaginationJsonResp(
        data=[await OrderGetter.parse_record(i) for i in orders],
        pagination=query.pagination
    )


@router.post(tags=[APITags.console], summary="手动触发订单钱包扣费")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "id": int,
        })
):
    await header.verify(Privileges.system_control)
    o = await Order.filter(id=query.id).first()
    if not o:
        raise NotFound("订单不存在")
    if o.status == OrderStatus.paid.value:
        raise Forbidden("订单已支付")

    customer_code = str(o.order_guanxi_id)
    amount = o.total_price
    if amount <= 0:
        o.status = OrderStatus.paid.value
        await o.save()
        return

    try:
        await WalletAccountService.consume(
            customer_code=customer_code,
            amount=amount,
            related_order_id=o.order_id,
            remark="订单手动扣费",
        )
        o.status = OrderStatus.paid.value
        await o.save()
    except Forbidden as e:
        o.status = OrderStatus.pay_failed.value
        await o.save()
        raise e
