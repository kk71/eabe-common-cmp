__all__ = [
    "UserGetter",
]

from typing import Any

from backend.core.tpdm import *
from backend.models import *


@init_t_pdm
class UserGetter(TGetter):
    role_ids: list[int]
    customer_name: str | None = None
    customer_code: str | None = None

    class TMeta:
        cls = User
        exclude = ("password",)

    @classmethod
    async def extra_fields(cls, t_inst: User, results: dict[str, Any]) -> None:
        results["role_ids"] = [i.role_id for i in await t_inst.user_roles.all()]
        c = await t_inst.customer
        if c:
            results["customer_name"] = c.name
            results["customer_code"] = c.code
        else:
            results["customer_name"] = None
            results["customer_code"] = None
