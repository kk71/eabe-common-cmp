from typing import Annotated

from fastapi import Header
from pydantic import BaseModel, Field
from decimal import Decimal

from backend.core.tpdm import *
from backend.apis import *
from backend.models import RandomConsumptionRule, ProductType
from backend.apis.auth.base import *


@init_t_pdm
class RandomConsumptionRuleGetter(TGetter):
    class TMeta:
        cls = RandomConsumptionRule


class RandomConsumptionRuleBody(BaseModel):
    enabled: bool = Field(default=True)
    customer_code: str
    customer_name: str | None = None
    product_type: str = Field(description="产品类型（ProductType 枚举值/名称）")
    min_amount: Decimal = Field(default=Decimal("0.00"))
    max_amount: Decimal = Field(default=Decimal("0.00"))
    interval_minutes: int = Field(default=60, ge=1, le=60 * 24)
    remark: str | None = None


def _parse_product_type(v: str) -> str:
    smv = ProductType.get(v)
    if smv:
        return smv.value
    smv = ProductType.get_by_name(v)
    if smv:
        return smv.value
    raise BadRequest(f"未知 product_type: {v}")


@router.get(tags=[APITags.console], summary="查询随机消费规则")
async def _(
    header: Annotated[HeaderToken, Header()],
    query: build_query(
        {
            "enabled": opt_query(bool),
            "customer_code": opt_query(str),
            "product_type": opt_query(ProductType.str_enum()),
        },
        pagination=True,
        keyword=True,
    ),
) -> PaginationJsonResp[list[RandomConsumptionRuleGetter]]:
    await header.verify(Privileges.system_control)
    rules = RandomConsumptionRule.filter(**query.model_dump())
    rules = query.query_keyword(rules, "customer_code", "customer_name", "remark")
    rules = await query.paginate(rules)
    return PaginationJsonResp(
        data=[await RandomConsumptionRuleGetter.parse_record(i) for i in rules],
        pagination=query.pagination,
    )


@router.post(tags=[APITags.console], summary="创建随机消费规则")
async def _(
    header: Annotated[HeaderToken, Header()],
    body: RandomConsumptionRuleBody,
) -> JsonResp[RandomConsumptionRuleGetter]:
    await header.verify(Privileges.system_control)
    product_type_v = _parse_product_type(body.product_type)

    rule = await RandomConsumptionRule.create(
        enabled=body.enabled,
        customer_code=body.customer_code,
        customer_name=body.customer_name,
        product_type=product_type_v,
        min_amount=body.min_amount,
        max_amount=body.max_amount,
        interval_minutes=body.interval_minutes,
        remark=body.remark,
    )
    return JsonResp(data=await RandomConsumptionRuleGetter.parse_record(rule))


@router.patch(tags=[APITags.console], summary="更新随机消费规则")
async def _(
    header: Annotated[HeaderToken, Header()],
    query: build_query({"id": int}),
    body: RandomConsumptionRuleBody,
) -> JsonResp[RandomConsumptionRuleGetter]:
    await header.verify(Privileges.system_control)
    rule = await RandomConsumptionRule.filter(id=query.id).first()
    if not rule:
        raise NotFound("规则不存在")

    product_type_v = _parse_product_type(body.product_type)
    rule.enabled = body.enabled
    rule.customer_code = body.customer_code
    rule.customer_name = body.customer_name
    rule.product_type = product_type_v
    rule.min_amount = body.min_amount
    rule.max_amount = body.max_amount
    rule.interval_minutes = body.interval_minutes
    rule.remark = body.remark
    await rule.save()
    return JsonResp(data=await RandomConsumptionRuleGetter.parse_record(rule))

