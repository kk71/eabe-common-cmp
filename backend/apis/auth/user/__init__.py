from typing import Annotated, Any

from fastapi import Header
from pydantic import BaseModel, Field

from backend.apis import *
from backend.models import *
from backend.apis.auth.base import *
from backend.t_pdm.system import *
from backend.core.validators import *
from backend.core.tpdm import *
from backend.services.auth import *


@init_t_pdm
class UserSetter(TSetter):
    role_ids: list[int]= Field(default_factory=list)

    class TMeta(SetterMeta):
        cls = User
        exclude = ("password",)

    async def after_saving(self, t_inst: User):
        await UserRole.filter(user=t_inst).delete()
        for i in self.role_ids:
            await UserRole.create(user=t_inst, role_id=i)


@router.get(tags=[APITags.auth], summary="查询用户")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "id": opt_query(str),
            "include_disabled": opt_query(bool, default=False, description="是否包含已禁用用户")
        }, keyword=True, pagination=True)
) -> PaginationJsonResp[list[UserGetter]]:
    await header.verify()
    d = query.model_dump()
    include_disabled = d.pop("include_disabled")
    q = User.filter(**d)
    if not include_disabled:
        q = q.filter(disabled=False)
    q = query.query_keyword(q, "name", "login_name", "id")
    r = await query.paginate(q)
    return PaginationJsonResp(
        data=[await UserGetter.parse_record(i) for i in r],
        pagination=query.pagination
    )


@router.post(tags=[APITags.system], summary="增加用户")
async def _(
        header: Annotated[HeaderToken, Header()],
        body: UserSetter
) -> JsonResp[UserGetter]:
    await header.verify(Privileges.system_control)
    u = User()
    await body.write_record(u)
    return JsonResp(data=await UserGetter.parse_record(u))


@router.patch(tags=[APITags.system], summary="修改用户")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "id": str,
        }),
        body: UserSetter
):
    await header.verify()
    u = await User.filter(id=query.id).first()
    if not u:
        raise NotFound("找不到用户")
    if u.id != header.user.id:
        await header.acquire(Privileges.system_control)
    await body.write_record(u)


@router.delete(tags=[APITags.system], summary="删除用户")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "id": opt_query(str),
            "id__in": opt_query(DotSplitStr)
        }, at_least_one=True),
):
    await header.verify(Privileges.system_control)
    q = User.filter(**query.model_dump())
    for u in await q:
        if u.id == header.user.id:
            raise Forbidden("无法删除当前登录用户。")
    if await q.count() == 1 and (await q.first()).is_admin and await User.filter(is_admin=True).count() == 1:
        raise Forbidden("仅有的一名管理员，不允许删除。")
    await q.delete()
