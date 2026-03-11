from typing import Annotated

from fastapi import Header

from backend.core.tpdm import *
from backend.apis import *
from backend.models import *
from backend.apis.auth.base import *


@init_t_pdm
class WalletAccountGetter(TGetter):
    class TMeta:
        cls = WalletAccount


@init_t_pdm
class WalletTransactionGetter(TGetter):
    class TMeta:
        cls = WalletTransaction


@router.get(tags=[APITags.buyer], summary="查询钱包账户（客户侧）")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "customer_code": opt_query(str),
        }, pagination=True, keyword=True)
) -> PaginationJsonResp[list[WalletAccountGetter]]:
    await header.verify()
    wallets = WalletAccount.filter(**query.model_dump())
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
    await header.verify()
    d = query.model_dump()
    customer_code = d.pop("customer_code", None)
    wallet_qs = WalletAccount.filter(customer_code=customer_code) if customer_code else WalletAccount.all()
    wallets = await wallet_qs
    wallet_ids = [w.id for w in wallets]
    if customer_code and not wallet_ids:
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

