from typing import Annotated

from fastapi import Header
from pydantic import BaseModel, Field

from backend.apis import *
from backend.apis.auth.base import *
from backend.apis.sell.auth import verify_sell_user
from backend.core.http import *
from backend.models import *


class CustomerSelfUpdateBody(BaseModel):
    name: str = Field(description="客户名")
    contact_phone: str | None = Field(default=None, description="联系电话")
    principal: str | None = Field(default=None, description="主要负责人")


class CustomerSelfView(BaseModel):
    id: int
    name: str
    contact_phone: str | None = None
    principal: str | None = None


async def _get_user_customer(header: HeaderToken) -> Customer:
    if header.user.is_admin:
        raise Forbidden("管理员不属于客户")
    c = await Customer.filter(id=getattr(header.user, "customer_id", None)).first()
    if not c:
        raise NotFound("未绑定客户")
    return c


@router.get(tags=[APITags.buyer], summary="查看当前用户所属客户信息（不含备注）")
async def _(
    header: Annotated[HeaderToken, Header()],
) -> JsonResp[CustomerSelfView]:
    await verify_sell_user(header)
    c = await _get_user_customer(header)
    return JsonResp(
        data=CustomerSelfView(
            id=c.id,
            name=c.name,
            contact_phone=c.contact_phone,
            principal=c.principal,
        )
    )


@router.patch(tags=[APITags.buyer], summary="修改当前用户所属客户信息（不含备注）")
async def _(
    header: Annotated[HeaderToken, Header()],
    body: CustomerSelfUpdateBody,
) -> JsonResp[CustomerSelfView]:
    await verify_sell_user(header)
    c = await _get_user_customer(header)
    c.name = body.name
    c.contact_phone = body.contact_phone
    c.principal = body.principal
    await c.save()
    return JsonResp(
        data=CustomerSelfView(
            id=c.id,
            name=c.name,
            contact_phone=c.contact_phone,
            principal=c.principal,
        )
    )

