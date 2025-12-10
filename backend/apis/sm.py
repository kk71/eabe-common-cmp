from typing import Any

from backend.core.status_machine.export import *
from backend.core.status_machine.status_machine import EXPORTED_STATUS_MACHINES
from . import *


@router.get(tags=[APITags.sm], summary="输出状态机全部值")
async def _() -> JsonResp[list[dict[str, Any]]]:
    return JsonResp(
        data=StatusMachineAPIBuilder(EXPORTED_STATUS_MACHINES).list_resp()
    )
