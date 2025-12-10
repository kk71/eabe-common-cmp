# Author: kk.Fang(fkfkbill@gmail.com)

__all__ = []

from typing import Type
from enum import StrEnum

import orjson
import aiohttp
from rich import print
from pydantic import BaseModel, constr, Field, ConfigDict


class MediaTypes(StrEnum):
    """常用media type"""
    # json
    application__json = "application/json"
    # 通用文件
    application__octet_stream = "application/octet-stream"
    # 纯文本
    text__plain = "text/plain"
    # 普通请求体key-value型
    application__x_www_form_urlencoded = "application/x-www-form-urlencoded"
    # 支持文件上传的请求体key-value型
    multipart__form_data = "multipart/form-data"


class HTTPRequestMethod(StrEnum):
    """常见http请求方法"""
    get = "get"
    post = "post"
    patch = "patch"
    put = "put"
    delete = "delete"


class BaseRequestPartition(BaseModel):

    def export(self, root: "BaseSDK", **kwargs) -> dict:
        """输出用于传给request的字典"""
        return self.model_dump(by_alias=True, exclude_none=True)


class BaseSDKHeader(BaseRequestPartition):
    model_config = ConfigDict(extra="allow")

    def export(self, root: "BaseSDK", **kwargs):
        r = super().export(root=root, **kwargs)
        if root.body:
            # 对于get方法是不存在body这个概念的
            r["Content-Type"] = root.body._content_type.value
        return r


class BaseSDKBody(BaseRequestPartition):
    """http请求体结构"""

    # 请求体类型
    _content_type: MediaTypes


class BaseSDKMultipartBody(BaseSDKBody):
    """支持文件上传的多行请求体数据"""

    _content_type: MediaTypes = MediaTypes.multipart__form_data


class BaseJsonSerializer:

    @classmethod
    def to_json_dict(cls, v):
        raise NotImplementedError


class BaseSDKJsonBody(BaseSDKBody):
    """json请求体数据"""

    _content_type: MediaTypes = MediaTypes.application__json

    _serializer: Type[BaseJsonSerializer] | None = None

    def export(self, root: "BaseSDK", to_json: bool = True, **kwargs) -> bytes | dict:
        """
        :param root:
        :param to_json: 是否直接输出json文本
        :param kwargs:
        """
        r = super().export(root=root, **kwargs)
        if self._serializer:
            r = self._serializer.to_json_dict(r)
        if to_json:
            return orjson.dumps(r)
        return r


class BaseSDK(BaseModel):
    """外部api的sdk"""

    # 数据结构
    query: BaseRequestPartition = Field(default=None)
    header: BaseSDKHeader = Field(default_factory=BaseSDKHeader)
    body: BaseSDKBody | None = Field(default=None)

    # url前缀
    prefix: constr(strip_whitespace=True)
    # 请求url
    request_url: constr(strip_whitespace=True)
    # 请求方法
    method: HTTPRequestMethod
    # 请求用的request session
    session: aiohttp.ClientSession | None = None
    # 如果没有指定session，则临时创建session
    _temp_session: aiohttp.ClientSession | None = None
    # 调试模式，调试模式会打印对应到requests的参数。
    debug: bool = False
    # 默认编码
    codec: str = "utf-8"

    model_config = ConfigDict(
        extra = "forbid",
        arbitrary_types_allowed = True
    )

    def _get_absolute_request_url(self) -> str:
        """请求绝对url"""
        prefix = self.prefix
        if prefix.endswith("/"):
            prefix = prefix[:-1]
        req_url = self.request_url
        if req_url.startswith("/"):
            req_url = req_url[1:]
        if not prefix:
            return req_url
        return f"{prefix}/{req_url}"

    def _ensure_encode(self, d):
        """编码"""
        if not d:
            return
        if isinstance(d, bytes):
            return d
        if isinstance(d, str):
            return d.encode(self.codec)
        return d

    def _gen_request_params(self) -> dict:
        r = dict(
            method=self.method,
            str_or_url=self._get_absolute_request_url(),
            params=self.query.export(self) if self.query else None,
            headers=self.header.export(self) if self.header else None,
            data=self._ensure_encode(self.body.export(self)) if self.body else None
        )
        # for k, v in r.items():
        #     if isinstance(v, str):
        #         r[k] = v.encode("utf-8")
        if self.debug:
            print(r)
        return r

    async def fire(self) -> aiohttp.ClientResponse:
        """发送请求，等待返回数据"""
        if not self.session:
            raise ValueError("fire method only available when session is set, "
                             "otherwise use async with statement instead")
        return await self.session._request(**self._gen_request_params())

    async def __aenter__(self) -> aiohttp.ClientResponse:
        session = self.session
        if not self.session:
            session = self._temp_session = aiohttp.ClientSession()
        return await session._request(**self._gen_request_params())

    async def __aexit__(self, exc_type, exc, tb):
        if self._temp_session and not self._temp_session.closed:
            await self._temp_session.close()


class BaseSDKSessionAdaptor:
    """
    requests的session适配器
    核心功能：
    1简化session复用功能
    2提供token过期/失效时的自动刷新

    TODO 不同sdk场景不同，需要单独完善具体实现
    """

    def __init__(self, **kwargs):
        self.session = aiohttp.ClientSession()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    def fire(self, target: Type["BaseSDK"], /, **kwargs):
        """
        拼装数据，发送请求
        :param target: 传入sdk的引用
        :param kwargs:
        :return:
        """
        target_inst = target(**kwargs)
        target_inst.session = self.session
        return target_inst.fire()
