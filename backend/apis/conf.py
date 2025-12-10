from pydantic import BaseModel, Field

from settings import backend_conf
from backend.apis import *


class SystemConfResp(BaseModel):
    debug: bool = backend_conf.debug
    prod_env: bool = backend_conf.prod_env


@router.get(tags=[APITags.system], summary="查询系统配置和当前运行模式")
async def _() -> JsonResp[SystemConfResp]:
    return JsonResp(
        data=SystemConfResp()
    )
