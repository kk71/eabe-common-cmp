from typing import Annotated

from fastapi import Header
from pydantic import Field
from decimal import Decimal

from backend.core.tpdm import *
from backend.apis import *
from backend.models import *
from backend.services import *
from backend.apis.auth.base import *


@init_t_pdm
class WalletAccountGetter(TGetter):
    class TMeta:
        cls = WalletAccount


@init_t_pdm
class WalletTransactionGetter(TGetter):
    class TMeta:
        cls = WalletTransaction


class WalletRechargeBody(BaseModel):
    """充值请求体"""
    customer_code: str = Field(description="客户编码")
    customer_name: str | None = Field(default=None, description="客户名称（可选，用于初始化或更新钱包账户名称）")
    amount: Decimal = Field(description="充值金额，>0")
    remark: str | None = Field(default=None, description="备注")

class WalletSetBalanceBody(BaseModel):
    """设置余额请求体（会自动生成充值/调整流水）"""
    customer_code: str = Field(description="客户编码")
    customer_name: str | None = Field(default=None, description="客户名称（可选，用于初始化或更新钱包账户名称）")
    balance: Decimal = Field(description="目标余额，>=0")
    remark: str | None = Field(default=None, description="备注")

async def _require_customer_by_code(customer_code: str) -> None:
    code = (customer_code or "").strip()
    if not code:
        raise BadRequest("customer_code 不能为空")
    if not await Customer.filter(existed=True, code=code).exists():
        raise BadRequest(f"客户不存在（客户编号={code}），请先在【客户支持-客户】中创建并配置客户编号")


@router.get(tags=[APITags.console], summary="查询钱包账户列表")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "customer_code": opt_query(str),
        }, pagination=True, keyword=True)
) -> PaginationJsonResp[list[WalletAccountGetter]]:
    await header.verify(Privileges.system_control)
    wallets = WalletAccount.filter(**query.model_dump())
    wallets = query.query_keyword(wallets, "customer_code", "customer_name")
    wallets = await query.paginate(wallets)
    return PaginationJsonResp(
        data=[await WalletAccountGetter.parse_record(i) for i in wallets],
        pagination=query.pagination
    )


@router.get(path_postfix="/tx", tags=[APITags.console], summary="查询钱包流水")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "wallet_id": opt_query(int),
            "customer_code": opt_query(str),
            "tx_type": opt_query(WalletTransactionType.str_enum()),
        }, pagination=True, keyword=True)
) -> PaginationJsonResp[list[WalletTransactionGetter]]:
    await header.verify(Privileges.system_control)
    d = query.model_dump()
    customer_code = d.pop("customer_code", None)
    wallet_qs = WalletAccount.filter(customer_code=customer_code) if customer_code else WalletAccount.all()
    wallets = await wallet_qs
    wallet_ids = [w.id for w in wallets]
    if customer_code and not wallet_ids:
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


@router.post(path_postfix="/recharge", tags=[APITags.console], summary="钱包充值")
async def _(
        header: Annotated[HeaderToken, Header()],
        body: WalletRechargeBody
) -> JsonResp[WalletAccountGetter]:
    await header.verify(Privileges.system_control)
    await _require_customer_by_code(body.customer_code)
    wallet = await WalletAccountService.recharge(
        customer_code=body.customer_code,
        customer_name=body.customer_name,
        amount=body.amount,
        remark=body.remark,
    )
    return JsonResp(data=await WalletAccountGetter.parse_record(wallet))


@router.post(path_postfix="/set-balance", tags=[APITags.console], summary="设置钱包余额（自动生成充值/调整记录）")
async def _(
        header: Annotated[HeaderToken, Header()],
        body: WalletSetBalanceBody
) -> JsonResp[WalletAccountGetter]:
    await header.verify(Privileges.system_control)
    await _require_customer_by_code(body.customer_code)
    wallet = await WalletAccountService.set_balance(
        customer_code=body.customer_code,
        customer_name=body.customer_name,
        target_balance=body.balance,
        remark=body.remark,
    )
    return JsonResp(data=await WalletAccountGetter.parse_record(wallet))
