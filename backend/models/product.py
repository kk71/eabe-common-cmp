
import uuid

from pydantic import BaseModel, Field

from backend.core.status_machine import *


class ProductType(StatusMachine):
    """产品类型"""
    EXPORT_FLAG = "product-type"
    stream = SMV("流量")
    sms = SMV("短信服务")
    gpu = SMV("GPU")
    ecs = SMV("ECS")
    bare_metal = SMV("裸金属服务器")
    cloud_computer = SMV("云电脑")
    digital_person = SMV("数字人")
    customized_server = SMV("定制化服务器")
    # cloud_communication_yw_sms = SMV("云通信异网短信服务")
    # cloud_communication_yw_bigdata_sms = SMV("云通信异网大数据短信服务")
    # cloud_tablet = SMV("云平板")


class Product(BaseModel):
    inst_id: str = Field(default_factory=lambda: uuid.uuid4().hex, description="实例id")
    type: ProductType.str_enum()

    @classmethod
    def parse(cls, d: dict):
        cls.model_validate(d)
        if d["type"] == ProductType.stream.value:
            return ProductStream.model_validate(d)
        elif d["type"] == ProductType.sms.value:
            return ProductSMS.model_validate(d)
        elif d["type"] == ProductType.gpu.value:
            return ProductGPU.model_validate(d)
        elif d["type"] == ProductType.ecs.value:
            return ProductECS.model_validate(d)
        elif d["type"] == ProductType.bare_metal.value:
            return ProductBareMetal.model_validate(d)
        elif d["type"] == ProductType.cloud_computer.value:
            return ProductCloudComputer.model_validate(d)
        else:
            raise ValueError(f"unsupported product type: {d["type"]}")


class ProductStreamQuantity(StatusMachine):
    """流量"""
    EXPORT_FLAG = "product-stream-quantity"
    stream_3g = SMV("3G")
    stream_5g = SMV("5G")
    stream_8g = SMV("8G")
    stream_10g = SMV("10G")
    stream_12g = SMV("12G")
    stream_20g = SMV("20G")
    stream_30g = SMV("30G")
    stream_50g = SMV("50G")
    stream_60g = SMV("60G")
    stream_120g = SMV("120G")


class ProductStreamPeriod(StatusMachine):
    """流量包周期"""
    EXPORT_FLAG = "product-stream-period"
    daily = SMV("日包")
    monthly = SMV("月包")
    semi_yearly = SMV("半年包")
    yearly = SMV("年包")


class ProductStream(Product):
    """流量"""
    type: ProductType.str_enum() = ProductType.stream.value
    target_phone_number: str
    period: ProductStreamPeriod.str_enum()
    quantity: ProductStreamQuantity.str_enum()


class ProductSMSPeriod(StatusMachine):
    """短信包周期"""
    EXPORT_FLAG = "product-sms-period"
    months_3 = SMV("3月")
    years_2 = SMV("2年")


class ProductSMSPackageType(StatusMachine):
    """短信包类型"""
    EXPORT_FLAG = "product-sms-type"
    domestic_common = SMV("国内通用短信")
    domestic_system = SMV("国内系统通知")


class ProductSMSResourceQuantity(StatusMachine):
    """短信包规格"""
    EXPORT_FLAG = "product-sms-quantity"
    q500 = SMV("500")
    q1000 = SMV("1000")
    q2000 = SMV("2000")
    q5000 = SMV("5000")
    q10000 = SMV("1万")
    q50000 = SMV("5万")
    q200000 = SMV("20万")
    q500000 = SMV("50万")
    q1000000 = SMV("100万")
    q3000000 = SMV("300万")


class ProductSMS(Product):
    """SMS"""
    type: ProductType.str_enum() = ProductType.sms.value
    package_type: ProductSMSPackageType.str_enum()
    resource_quantity: ProductSMSResourceQuantity.str_enum()
    period: ProductSMSPeriod.str_enum()


class ProductGPU(Product):
    """GPU"""
    type: ProductType.str_enum() = ProductType.gpu.value


class ProductECS(Product):
    """ECS"""


class ProductBareMetal(Product):
    """裸金属"""
    type: ProductType.str_enum() = ProductType.bare_metal.value


class ProductCloudComputer(Product):
    """云电脑"""
    type: ProductType.str_enum() = ProductType.cloud_computer.value