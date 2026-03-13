from typing import Annotated, Any

from fastapi import Header

from backend.core.tpdm import *
from backend.apis import *
from backend.models import *
from backend.services.auth import *
from backend.apis.auth.base import *
from backend.apis.sell.auth import verify_sell_user
from backend.core.http import Forbidden
from backend.t_pdm.customer import CustomerGetter


@init_t_pdm
class OrderGetter(TGetter):
    customer: CustomerGetter | None = None

    class TMeta:
        cls = Order

    @classmethod
    async def extra_fields(cls, t_inst: Order, results: dict[str, Any]) -> None:
        # buyer 侧也返回 customer（按 customer_code 关联）
        code = (getattr(t_inst, "customer_code", None) or "").strip()
        if not code:
            results["customer"] = None
            return
        c = await Customer.filter(existed=True, code=code).first()
        results["customer"] = await CustomerGetter.parse_record(c) if c else None


async def _get_bound_customer_code(header: HeaderToken) -> str:
    """
    获取当前登录用户绑定客户的 customer_code（客户侧后台专用）。
    仅允许访问自己所属客户的数据。
    """
    user = header.user
    customer_id = getattr(user, "customer_id", None)
    if not customer_id:
        raise Forbidden("当前登录用户未绑定客户")
    customer = await Customer.filter(existed=True, id=customer_id).first()
    if not customer or not (customer.code or "").strip():
        raise Forbidden("当前登录用户绑定的客户不存在或未配置客户编号")
    return customer.code.strip()


@router.get(tags=[APITags.buyer], summary="查询订单")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "id": opt_query(int),
            "order_id": opt_query(str),
            "customer_code": opt_query(str),
            "product_type": opt_query(ProductType.str_enum()),
            "status": opt_query(OrderStatus.str_enum()),
            "origin": opt_query(OrderOrigin.str_enum()),
        }, pagination=True, keyword=True)
) -> PaginationJsonResp[list[OrderGetter]]:
    await verify_sell_user(header)
    # 订单仅允许查询当前登录用户绑定客户的数据
    customer_code = await _get_bound_customer_code(header)
    d = query.model_dump()
    # 强制使用绑定客户的 customer_code，忽略外部传入的 customer_code
    d["customer_code"] = customer_code
    orders = Order.filter(**d)
    orders = query.query_keyword(orders, "order_id", "customer_code", "batch_code", "product_name", "resource_code")
    orders = await query.paginate(orders)
    return PaginationJsonResp(
        data=[await OrderGetter.parse_record(i) for i in orders],
        pagination=query.pagination
    )
