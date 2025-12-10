from typing import Annotated, Any

from fastapi import Header

from backend.core.tpdm import *
from backend.apis import *
from backend.models import *
from backend.apis.auth.base import *


@init_t_pdm
class CartGetter(TGetter):
    class TMeta:
        cls = Cart


@router.get(tags=[APITags.buyer], summary="查询用户购物车")
async def _(
        header: Annotated[HeaderToken, Header()],
) -> JsonResp[CartGetter]:
    await header.verify()
    the_cart = await Cart.filter(user_id=header.user.id).first()
    if not the_cart:
        the_cart = Cart(user=header.user)
        await the_cart.save()
    return JsonResp(
        data=await CartGetter.parse_record(the_cart)
    )


@init_t_pdm
class CartSetter(TSetter):
    class TMeta(SetterMeta):
        cls = Cart
        exclude = ("user_id",)


@router.patch(path_postfix="/add", tags=[APITags.buyer], summary="加入购物车")
async def _(
        header: Annotated[HeaderToken, Header()],
        body: dict
):
    await header.verify()
    the_cart = await Cart.filter(user_id=header.user.id).first()
    if not the_cart:
        the_cart = Cart(user=header.user)
        await the_cart.save()
    the_cart = await Cart.filter(user_id=header.user.id).first()
    the_cart.detail.push(Product.parse(body))


class CartDeleteProductBody(BaseModel):
    inst_id: str


@router.patch(path_postfix="/delete", tags=[APITags.buyer], summary="从购物车去除")
async def _(
        header: Annotated[HeaderToken, Header()],
        body: CartDeleteProductBody
):
    await header.verify()
    the_cart = await Cart.filter(user_id=header.user.id).first()
    new_detail = []
    for p in the_cart.detail:
        if p.inst_id != body.inst_id:
            new_detail.append(p)
    the_cart.detail = new_detail
    await the_cart.save()
