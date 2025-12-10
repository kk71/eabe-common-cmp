__all__ = [
    "AuthTokenOrigin",
    "UserAuthService",
    "Privileges",
    "RootPrivilegeGroup",
    "PrivilegeUnmet",
]

import time
import hashlib
from typing import Optional, Any
from enum import StrEnum

import jwt
from jwt.exceptions import DecodeError
from loguru import logger
from pydantic import BaseModel, Field, ConfigDict

from backend.core.http import *
from backend.models import *
from backend.core.privilege import *
from settings import backend_conf


class PrivilegeUnmet(Forbidden):
    """权限不足"""


class Privileges(PrivilegeSet):
    """全部权限"""
    system_control = Privilege(title="可进入管理后台")


# 全部权限归纳的分组
RootPrivilegeGroup = PrivilegeGroup(
    title="所有权限",
    children=[
        Privileges.system_control,
    ]
)


class AuthTokenOrigin(StrEnum):
    """token生成来源"""
    password = "password"


class UserTokenJwt(BaseModel):
    """用于输出和校验jwt的解构"""
    id: str = Field(description="用户唯一id")
    timestamp: int = Field(description="jwt生成时间")
    user_agent: str = Field(description="生成jwt的user-agent值")
    origin: AuthTokenOrigin
    model_config = ConfigDict(extra="allow")

    def build(self) -> str:
        return jwt.encode(self.model_dump(), backend_conf.jwt_key, algorithm="HS256")

    @classmethod
    def parse(cls, t: str) -> Optional["UserTokenJwt"]:
        if not t:
            raise Unauthorized(f"未登录")
        try:
            d = jwt.decode(t, backend_conf.jwt_key, algorithms=["HS256"])
        except DecodeError as e:
            raise Unauthorized(f"token无效：{e}")
        return cls.model_validate(d)


class UserAuthService:
    """后台用户登录管理"""

    def __init__(self, u: User):
        self.user = u

    async def set_new_password(self, new_password: str):
        """
        设置新密码
        :param new_password: 请注意这个密码是明文。
        :return:
        """
        self.user.password = hashlib.sha512(new_password.encode()).hexdigest()
        await self.user.save()

    def generate_token(self, user_agent: str, origin: AuthTokenOrigin) -> str:
        """生成token"""
        return UserTokenJwt(
            id=self.user.id,
            timestamp=int(time.time()),
            user_agent=user_agent,
            origin=origin
        ).build()

    def renew_token(self, token: str) -> str:
        """
        刷新token
        :param token:
        """
        if token.lower().startswith(b := "bearer "):
            token = token[len(b):]
        j = UserTokenJwt.parse(token)
        if self.user.disabled:
            raise Forbidden("用户已禁用")
        return self.generate_token(user_agent=j.user_agent, origin=j.origin)

    async def mark_disabled(self):
        """标记禁用"""
        self.user.disabled = True
        await self.user.save()

    @property
    def is_admin(self) -> bool:
        """是否最高级管理者"""
        return self.user.is_admin

    async def get_all_privileges(self) -> list[Privilege]:
        """返回用户的全部权限"""
        if self.is_admin:
            return Privileges.all()
        privilege_names = set()
        for i in await UserRole.filter(user=self.user).prefetch_related("role"):
            privilege_names.update(i.role.privileges)
        results = []
        for pn in privilege_names:
            p = Privileges.get(pn)
            if not p:
                logger.warning(f"deleted privilege but is still saved in DB: {pn} bound to {self.user}")
                continue
            results.append(p)
        return results

    async def has_privilege(self, *privilege) -> bool:
        """判断是否拥有某个/某些权限"""
        try:
            await self.acquire_privilege(*privilege)
        except PrivilegeUnmet:
            return False
        return True

    async def acquire_privilege(self, *privilege):
        """要求拥有某个/某些权限"""
        all_privileges = await self.get_all_privileges()
        for p in privilege:
            if p not in all_privileges:
                raise PrivilegeUnmet(p)

    @classmethod
    async def password_login(cls,
                             login_name: str,
                             password: str) -> Optional["UserAuthService"]:
        """
        密码登录
        :param login_name:
        :param password: 加密后的密码
        """
        u = await User.filter(login_name=login_name, password=password).first()
        if not u:
            raise Forbidden("用户名或密码错误")
        if u.disabled:
            raise Forbidden("用户已禁用")
        return cls(u)

    @classmethod
    async def verify_token(cls, token: str, user_agent: str) -> Optional["UserAuthService"]:
        """
        验证给出的token是否正确
        :param token:
        :param user_agent:
        """
        if token.lower().startswith(b := "bearer "):
            token = token[len(b):]
        j = UserTokenJwt.parse(token)
        if j.user_agent != user_agent or (time.time() - j.timestamp) > backend_conf.jwt_timeout:
            raise Unauthorized("token无效")
        u = await User.filter(id=j.id).first()
        if not u:
            raise Unauthorized("用户不存在")
        return cls(u)
