from typing import Annotated, Any

from fastapi import Header

from backend.apis import *
from backend.core.tpdm import *
from backend.core.validators import *
from backend.models import *
from backend.apis.auth.base import *
from backend.services import Privileges


@init_t_pdm
class RoleGetter(TGetter):
    class TMeta:
        cls = Role


@init_t_pdm
class RoleSetter(TSetter):
    class TMeta(SetterMeta):
        cls = Role


@router.get(tags=[APITags.auth], summary="查询角色")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "id": opt_query(str),
        })
) -> JsonResp[list[RoleGetter]]:
    await header.verify()
    r = await Role.filter(**query.model_dump())
    return JsonResp(
        data=[await RoleGetter.parse_record(i) for i in r],
    )


@router.post(tags=[APITags.auth], summary="创建角色")
async def _(
        header: Annotated[HeaderToken, Header()],
        body: RoleSetter
):
    await header.verify(Privileges.system_control)
    await body.write_record(Role())


@router.patch(tags=[APITags.auth], summary="修改角色")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({"id": int}),
        body: RoleSetter
):
    await header.verify(Privileges.system_control)
    r = await Role.filter(**query.model_dump()).get()
    await body.write_record(r)


@router.delete(tags=[APITags.auth], summary="删除角色")
async def _(
        header: Annotated[HeaderToken, Header()],
        query: build_query({
            "id": opt_query(int),
            "id__in": opt_query(DotSplitInt)
        }, at_least_one=True),
):
    await header.verify(Privileges.system_control)
    await Role.filter(**query.model_dump()).delete()
