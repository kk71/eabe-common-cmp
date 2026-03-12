__all__ = [
    "CustomerGetter",
]

from typing import Any

from backend.core.tpdm import *
from backend.models import *


@init_t_pdm
class CustomerGetter(TGetter):
    user_ids: list[str]

    class TMeta:
        cls = Customer

    @classmethod
    async def extra_fields(cls, t_inst: Customer, results: dict[str, Any]) -> None:
        users = await t_inst.users.all()
        results["user_ids"] = [u.id for u in users]

