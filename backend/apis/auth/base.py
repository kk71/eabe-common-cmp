__all__ = [
    "HeaderToken",
]

from backend.core.http import *
from backend.services.auth import *
from backend.models import *


class HeaderToken(BaseHeaderToken):
    user_agent: str
    _user_auth_service: UserAuthService | None = None

    async def verify(self, *any_privileges) -> bool:
        """
        验证后台登录的用户，如果给出权限，则一并验证权限是否满足
        :param any_privileges:
        :return:
        """
        s = await UserAuthService.verify_token(
            token=self.authorization, user_agent=self.user_agent)
        await s.acquire_privilege(*any_privileges)
        self._user_auth_service = s
        return True

    @property
    def user_auth(self) -> UserAuthService | None:
        if not self._user_auth_service:
            raise Unauthorized("未登录")
        return self._user_auth_service

    @property
    def user(self) -> User:
        return self.user_auth.user

    async def has(self, *privileges) -> bool:
        return await self.user_auth.has_privilege(*privileges)

    async def acquire(self, *privileges):
        await self.user_auth.acquire_privilege(*privileges)
