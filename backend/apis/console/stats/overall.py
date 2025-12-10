from typing import Annotated, Any

from fastapi import Header

from backend.core.tpdm import *
from backend.apis import *
from backend.models import *
from backend.services.auth import *
from backend.apis.auth.base import *


class ProductStatsData(BaseModel):
    product_type: ProductType.str_enum()
    product_name: str
    count: int = Field(description="售出数量")
    amount: float = Field(description="总金额")


@router.get(tags=[APITags.console], summary="全景统计")
async def _(
        header: Annotated[HeaderToken, Header()],
) -> JsonResp[list[ProductStatsData]]:
    await header.verify(Privileges.system_control)
    return JsonResp(
        data=[
            ProductStatsData(
                product_type=ProductType.stream.value, product_name=ProductType.stream.name,
                count=256, amount="35609"),
            ProductStatsData(
                product_type=ProductType.sms.value, product_name=ProductType.sms.name,
                count=256, amount="35609"),
            ProductStatsData(
                product_type=ProductType.gpu.value, product_name=ProductType.gpu.name,
                count=256, amount="35609"),
            ProductStatsData(
                product_type=ProductType.ecs.value, product_name=ProductType.ecs.name,
                count=256, amount="35609"),
            ProductStatsData(
                product_type=ProductType.bare_metal.value, product_name=ProductType.bare_metal.name,
                count=114, amount="35609"),
            ProductStatsData(
                product_type=ProductType.cloud_computer.value, product_name=ProductType.cloud_computer.name,
                count=122, amount="35609"),
        ]
    )
