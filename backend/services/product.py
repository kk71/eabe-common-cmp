__all__ = [
    "ProductInfo",
    "get_product_info",
]
from typing import Any

from pydantic import BaseModel

from backend.models import *


class ProductPrice(BaseModel):
    """产品对应配置的价格"""
    product: Any
    price: float


class ProductPriceCalc:
    KEYS_TO_CALC: list[str]
    MAPPING: list[ProductPrice]

    @classmethod
    def get_price(cls, p: Product) -> float | None:
        """查询价格"""
        for i in cls.MAPPING:
            if all([getattr(i.product, k) == getattr(p, k) for k in cls.KEYS_TO_CALC]):
                return i.price

    @classmethod
    def get_desc(cls, p: Product) -> str | None:
        """查询一段式的描述"""
        raise NotImplementedError


class StreamPrice(ProductPriceCalc):

    KEYS_TO_CALC = ["period", "quantity"]

    @classmethod
    def get_desc(cls, p: ProductStream) -> str | None:
        s = [
            ProductStreamPeriod.get(p.period).name,
            ProductStreamQuantity.get(p.quantity).name,
        ]
        return " - ".join(s)

    MAPPING = [
        ProductPrice(
            product=ProductStream(
                target_phone_number="",
                period=ProductStreamPeriod.daily.value,
                quantity=ProductStreamQuantity.stream_5g.value
            ),
            price=5
        ),
        ProductPrice(
            product=ProductStream(
                target_phone_number="",
                period=ProductStreamPeriod.daily.value,
                quantity=ProductStreamQuantity.stream_10g.value
            ),
            price=10
        ),
        ProductPrice(
            product=ProductStream(
                target_phone_number="",
                period=ProductStreamPeriod.monthly.value,
                quantity=ProductStreamQuantity.stream_3g.value
            ),
            price=30
        ),
        ProductPrice(
            product=ProductStream(
                target_phone_number="",
                period=ProductStreamPeriod.monthly.value,
                quantity=ProductStreamQuantity.stream_8g.value
            ),
            price=50
        ),
        ProductPrice(
            product=ProductStream(
                target_phone_number="",
                period=ProductStreamPeriod.monthly.value,
                quantity=ProductStreamQuantity.stream_12g.value
            ),
            price=70
        ),
        ProductPrice(
            product=ProductStream(
                target_phone_number="",
                period=ProductStreamPeriod.monthly.value,
                quantity=ProductStreamQuantity.stream_20g.value
            ),
            price=100
        ),
        ProductPrice(
            product=ProductStream(
                target_phone_number="",
                period=ProductStreamPeriod.monthly.value,
                quantity=ProductStreamQuantity.stream_30g.value
            ),
            price=150
        ),
        ProductPrice(
            product=ProductStream(
                target_phone_number="",
                period=ProductStreamPeriod.semi_yearly.value,
                quantity=ProductStreamQuantity.stream_30g.value
            ),
            price=180
        ),
        ProductPrice(
            product=ProductStream(
                target_phone_number="",
                period=ProductStreamPeriod.semi_yearly.value,
                quantity=ProductStreamQuantity.stream_60g.value
            ),
            price=300
        ),
        ProductPrice(
            product=ProductStream(
                target_phone_number="",
                period=ProductStreamPeriod.yearly.value,
                quantity=ProductStreamQuantity.stream_60g.value
            ),
            price=360
        ),
        ProductPrice(
            product=ProductStream(
                target_phone_number="",
                period=ProductStreamPeriod.yearly.value,
                quantity=ProductStreamQuantity.stream_120g.value
            ),
            price=600
        ),
    ]


class SMSPrice(ProductPriceCalc):

    KEYS_TO_CALC = ["package_type", "resource_quantity", "period"]

    @classmethod
    def get_desc(cls, p: ProductSMS) -> str | None:
        s = [
            ProductSMSPackageType.get(p.package_type).name,
            ProductSMSResourceQuantity.get(p.resource_quantity).name,
            ProductSMSPeriod.get(p.period).name,
        ]
        return " - ".join(s)

    MAPPING = [
        ProductPrice(
            product=ProductSMS(
                package_type=ProductSMSPackageType.domestic_common.value,
                resource_quantity=ProductSMSResourceQuantity.q1000.value,
                period=ProductSMSPeriod.months_3.value
            ),
            price=3
        ),
    ]


class GPUPrice(ProductPriceCalc):

    KEYS_TO_CALC = []

    @classmethod
    def get_desc(cls, p: ProductGPU) -> str | None:
        s = [
        ]
        return " - ".join(s)

    MAPPING = [
    ]


class ECSPrice(ProductPriceCalc):

    KEYS_TO_CALC = []

    @classmethod
    def get_desc(cls, p: ProductGPU) -> str | None:
        s = [
        ]
        return " - ".join(s)

    MAPPING = [
    ]


class BareMetalPrice(ProductPriceCalc):

    KEYS_TO_CALC = []

    @classmethod
    def get_desc(cls, p: ProductGPU) -> str | None:
        s = [
        ]
        return " - ".join(s)

    MAPPING = [
    ]


class CloudComputerPrice(ProductPriceCalc):

    KEYS_TO_CALC = []

    @classmethod
    def get_desc(cls, p: ProductGPU) -> str | None:
        s = [
        ]
        return " - ".join(s)

    MAPPING = [
    ]


class ProductInfo(BaseModel):
    price: float | None
    desc: str | None


def get_product_info(p: Product) -> ProductInfo:
    """查询产品价格和额外信息"""
    if isinstance(p, ProductStream):
        return ProductInfo(price=StreamPrice.get_price(p), desc=StreamPrice.get_desc(p))
    elif isinstance(p, ProductSMS):
        return ProductInfo(price=SMSPrice.get_price(p), desc=SMSPrice.get_desc(p))
    elif isinstance(p, ProductGPU):
        return ProductInfo(price=SMSPrice.get_price(p), desc=SMSPrice.get_desc(p))
    elif isinstance(p, ProductECS):
        return ProductInfo(price=SMSPrice.get_price(p), desc=SMSPrice.get_desc(p))
    elif isinstance(p, ProductBareMetal):
        return ProductInfo(price=SMSPrice.get_price(p), desc=SMSPrice.get_desc(p))
    elif isinstance(p, ProductCloudComputer):
        return ProductInfo(price=SMSPrice.get_price(p), desc=SMSPrice.get_desc(p))
    else:
        raise ValueError(f"unsupported product type: {p}")
