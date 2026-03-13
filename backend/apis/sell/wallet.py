from typing import Annotated

from fastapi import Header

from backend.core.tpdm import *
from backend.apis import *
from backend.models import *
from backend.apis.auth.base import *
from backend.apis.sell.auth import verify_sell_user
from backend.core.http import Forbidden


@init_t_pdm
class WalletAccountGetter(TGetter):
    class TMeta:
        cls = WalletAccount


@init_t_pdm
class WalletTransactionGetter(TGetter):
    class TMeta:
        cls = WalletTransaction


async def _get_bound_customer_code(header: HeaderToken) -> str:
    """
    获取当前登录用户绑定客户的 customer_code（客户侧后台专用）。
    收支相关接口仅允许访问自己所属客户的数据。
    """
    user = header.user
    customer_id = getattr(user, "customer_id", None)
    if not customer_id:
        raise Forbidden("当前登录用户未绑定客户")
    customer = await Customer.filter(existed=True, id=customer_id).first()
    if not customer or not (customer.code or "").strip():
        raise Forbidden("当前登录用户绑定的客户不存在或未配置客户编号")
    return customer.code.strip()


@router.get(tags=[APITags.buyer], summary="查询钱包账户（客户侧）")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "customer_code": opt_query(str),
        }, pagination=True, keyword=True)
) -> PaginationJsonResp[list[WalletAccountGetter]]:
    await verify_sell_user(header)
    # 钱包账户仅允许查询当前登录用户绑定客户的数据
    customer_code = await _get_bound_customer_code(header)
    d = query.model_dump()
    # 强制使用绑定客户的 customer_code，忽略外部传入的 customer_code
    d["customer_code"] = customer_code
    wallets = WalletAccount.filter(**d)
    wallets = query.query_keyword(wallets, "customer_code", "customer_name")
    wallets = await query.paginate(wallets)
    return PaginationJsonResp(
        data=[await WalletAccountGetter.parse_record(i) for i in wallets],
        pagination=query.pagination
    )


@router.get(path_postfix="/tx", tags=[APITags.buyer], summary="查询钱包流水（客户侧）")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "wallet_id": opt_query(int),
            "customer_code": opt_query(str),
            "tx_type": opt_query(WalletTransactionType.str_enum()),
        }, pagination=True, keyword=True)
) -> PaginationJsonResp[list[WalletTransactionGetter]]:
    await verify_sell_user(header)
    # 钱包流水仅允许查询当前登录用户绑定客户的数据
    customer_code = await _get_bound_customer_code(header)
    d = query.model_dump()
    # 忽略外部传入的 customer_code，始终按绑定客户过滤
    d.pop("customer_code", None)
    wallet_qs = WalletAccount.filter(customer_code=customer_code)
    wallets = await wallet_qs
    wallet_ids = [w.id for w in wallets]
    if not wallet_ids:
        await query.paginate([])
        return PaginationJsonResp(data=[], pagination=query.pagination)

    if wallet_ids and "wallet_id" not in d:
        d["wallet_id__in"] = wallet_ids

    txs = WalletTransaction.filter(**d)
    txs = query.query_keyword(txs, "tx_id", "remark", "related_order_id", "related_bill_id")
    txs = await query.paginate(txs)
    return PaginationJsonResp(
        data=[await WalletTransactionGetter.parse_record(i) for i in txs],
        pagination=query.pagination
    )

