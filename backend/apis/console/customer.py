from typing import Annotated

from fastapi import Header
from pydantic import BaseModel, Field

from backend.apis import *
from backend.apis.auth.base import *
from backend.core.tpdm import *
from backend.core.validators import *
from backend.models import *
from backend.services import Privileges
from backend.t_pdm.customer import CustomerGetter


@init_t_pdm
class CustomerSetter(TSetter):
    user_ids: list[str] = Field(default_factory=list, description="绑定的登录用户id（不允许管理员）")

    class TMeta(SetterMeta):
        cls = Customer

    async def after_saving(self, t_inst: Customer):
        user_ids = [i for i in (self.user_ids or []) if i]
        if not user_ids:
            # 清空绑定
            await User.filter(customer=t_inst).update(customer=None)
            return

        users = await User.filter(id__in=user_ids).all()
        found_ids = {u.id for u in users}
        missing = [i for i in user_ids if i not in found_ids]
        if missing:
            raise BadRequest(f"用户不存在: {', '.join(missing)}")

        admins = [u.id for u in users if u.is_admin]
        if admins:
            raise BadRequest(f"不允许绑定管理员用户: {', '.join(admins)}")

        # 用户只能属于一个客户：先解绑这些用户原本所属客户，再绑定到当前客户
        await User.filter(id__in=user_ids).update(customer=t_inst)
        # 移除之前绑定但现在不在列表里的用户
        await User.filter(customer=t_inst).exclude(id__in=user_ids).update(customer=None)


class CustomerCreateBody(BaseModel):
    code: str = Field(description="客户编号（导入唯一标识）")
    name: str = Field(description="客户名")
    contact_phone: str | None = Field(default=None, description="联系电话")
    principal: str | None = Field(default=None, description="主要负责人")
    remark: str | None = Field(default=None, description="备注")
    user_ids: list[str] = Field(default_factory=list, description="绑定的登录用户id（不允许管理员）")


@router.get(tags=[APITags.console], summary="查询客户列表")
async def _(
    header: Annotated[HeaderToken, Header()],
    query: build_query(
        {
            "id": opt_query(int),
        },
        pagination=True,
        keyword=True,
    )
) -> PaginationJsonResp[list[CustomerGetter]]:
    await header.verify(Privileges.system_control)
    qs = Customer.filter(**query.model_dump())
    qs = query.query_keyword(qs, "name", "contact_phone", "principal")
    items = await query.paginate(qs)
    return PaginationJsonResp(
        data=[await CustomerGetter.parse_record(i) for i in items],
        pagination=query.pagination,
    )


@router.get(path_postfix="/detail", tags=[APITags.console], summary="查询客户详情")
async def _(
    header: Annotated[HeaderToken, Header()],
    query: build_query({"id": int}),
) -> JsonResp[CustomerGetter]:
    await header.verify(Privileges.system_control)
    c = await Customer.filter(id=query.id).first()
    if not c:
        raise NotFound("客户不存在")
    return JsonResp(data=await CustomerGetter.parse_record(c))


@router.post(tags=[APITags.console], summary="创建客户")
async def _(
    header: Annotated[HeaderToken, Header()],
    body: CustomerCreateBody,
) -> JsonResp[CustomerGetter]:
    await header.verify(Privileges.system_control)
    if not (body.code or "").strip():
        raise BadRequest("客户编号不能为空")
    if await Customer.filter(existed=True, code=body.code.strip()).exists():
        raise BadRequest("客户编号已存在")
    c = Customer()
    setter = CustomerSetter.model_validate(body.model_dump())
    await setter.write_record(c)
    return JsonResp(data=await CustomerGetter.parse_record(c))


@router.patch(tags=[APITags.console], summary="修改客户")
async def _(
    header: Annotated[HeaderToken, Header()],
    query: build_query({"id": int}),
    body: CustomerCreateBody,
) -> JsonResp[CustomerGetter]:
    await header.verify(Privileges.system_control)
    c = await Customer.filter(id=query.id).first()
    if not c:
        raise NotFound("客户不存在")
    if not (body.code or "").strip():
        raise BadRequest("客户编号不能为空")
    code = body.code.strip()
    if await Customer.filter(existed=True, code=code).exclude(id=c.id).exists():
        raise BadRequest("客户编号已存在")
    setter = CustomerSetter.model_validate(body.model_dump())
    await setter.write_record(c)
    return JsonResp(data=await CustomerGetter.parse_record(c))


@router.delete(tags=[APITags.console], summary="删除客户")
async def _(
    header: Annotated[HeaderToken, Header()],
    query: build_query({"id": opt_query(int), "id__in": opt_query(DotSplitInt)}, at_least_one=True),
) -> JsonResp[None]:
    await header.verify(Privileges.system_control)
    qs = Customer.filter(**query.model_dump())
    customers = await qs
    # 删除前先禁用并解绑用户
    for c in customers:
        await User.filter(customer=c).update(customer=None, disabled=True)
    await qs.delete()
    return JsonResp()

