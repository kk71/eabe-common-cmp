from typing import Annotated, Any

from fastapi import Header
from pydantic import ValidationError

from backend.apis import *
from backend.models import *
from backend.apis.auth.base import *
from backend.services import *


@router.post(path_postfix="/calc", tags=[APITags.buyer], summary="计算产品价格和描述信息")
async def _(
        header: Annotated[HeaderToken, Header()],
        body: dict
) -> JsonResp[ProductInfo]:
    # await header.verify()
    try:
        product_info = get_product_info(Product.parse(body))
        return JsonResp(data=product_info)
    except ValidationError:
        return JsonResp(data=ProductInfo(price=None, desc=None))
