from typing import Annotated, Any

from pydantic import BaseModel, Field
from fastapi import Header

from backend.apis import *
from backend.models import *
from backend.apis.auth.base import *
from backend.services.auth import *


class PasswordChangeBody(BaseModel):
    id: str
    old_password: str | None = None
    new_password: str


@router.patch(tags=[APITags.system], summary="修改登录密码")
async def _(
        header: Annotated[HeaderToken, Header()],
        body: PasswordChangeBody
):
    await header.verify()
    u = await User.filter(id=body.id).first()
    if not u:
        raise NotFound("用户不存在")
    if u.id != header.user.id:
        # 只有拥有权限才能给别的用户设置密码
        await header.acquire(Privileges.system_control)
    if not body.old_password:
        # 只有拥有权限才可以不指定旧密码而直接设置新密码
        await header.acquire(Privileges.system_control)
    if body.old_password and u.password != body.old_password:
        raise BadRequest("旧密码错误")
    u.password = body.new_password
    await u.save()
