from typing import Annotated, Any

from fastapi import Header, Request
from pydantic import BaseModel, Field

from backend.core.privilege import *
from backend.apis import *
from backend.t_pdm.system import *
from backend.services.auth import *


class PasswordLoginBody(BaseModel):
    login_name: str
    password: str


class LoginResult(BaseModel):
    """登录结果"""
    token: str
    user: UserGetter
    privileges: list[Privilege]


@router.post(tags=[APITags.auth], summary="密码登录，或者刷新token")
async def _(
        req: Request,
        body: PasswordLoginBody | dict
) -> JsonResp[LoginResult]:
    if isinstance(body, PasswordLoginBody):
        s = await UserAuthService.password_login(
            body.login_name,
            body.password
        )
        token = s.generate_token(
            user_agent=req.headers.get("User-Agent"),
            origin=AuthTokenOrigin.password
        )
    elif isinstance(body, dict):
        s = await UserAuthService.verify_token(req.headers.get("Authorization"), req.headers.get("User-Agent"))
        token = s.renew_token(req.headers.get("Authorization"))
    else:
        assert 0
    return JsonResp(
        data=LoginResult(
            token=token,
            user=await UserGetter.parse_record(s.user),
            privileges=await s.get_all_privileges()
        )
    )
