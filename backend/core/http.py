__all__ = [
    "opt_query",
    "build_query",
    "JsonResp",
    "PaginationJsonResp",
    "Pagination",
    "BaseHeaderToken",
    "CollectAPIRouter",
    "HttpError",
    "BadRequest",
    "Unauthorized",
    "Forbidden",
    "NotFound",
    "ServerError",
]

import uuid
from enum import StrEnum
from typing import Any, Type, Annotated, TypeVar, Generic, Callable, Sized

from pydantic import (BaseModel as pdm,
                      create_model, model_validator, Field, BeforeValidator, ConfigDict)
from fastapi import Query, Header, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from tortoise.queryset import AwaitableQuery, QuerySet, RawSQLQuery, Q
from tortoise import Model as TModel

from .cls_utils import *


def opt_query(t, **kwargs):
    """
    URL中参数不存在，或者值为空文本时，直接忽略该字段，
    忽略逻辑在model_dump内重载实现。
    如果需要指定默认值，请在kwargs传入default，请注意default_factory会被忽略
    :param t:
    :param kwargs:
    :return:
    """
    kwargs.setdefault("default", None)
    return Annotated[t | None, BeforeValidator(lambda v: v if v else kwargs["default"]), Field(**kwargs)]


class RequestQuery(pdm):
    """url query请求"""

    model_config = ConfigDict(coerce_numbers_to_str=True)

    def model_dump(self, *args, **kwargs) -> dict[str, Any]:
        if kwargs.get("exclude_none", None) is None:
            kwargs["exclude_none"] = True # ignore any None values(include default None)
        return super().model_dump(*args, **kwargs)


class RequestJsonQueryModify(pdm):
    """json内部query+modify请求"""
    query: dict | None = None
    modify: dict | list | None = None


class Pagination(pdm):
    page: int = Field(1, description="请求页")
    per_page: int = Field(10, description="每页数量")
    total: int = Field(0, description="数据总量")


class RequestPaginationMixin(pdm):
    """分页信息指定"""
    page: int = Field(1, description="请求页")
    per_page: int = Field(10, description="每页数量")
    _pagination: Pagination = None # 分页结果信息暂存

    def model_dump(self, *args, **kwargs) -> dict[str, Any]:
        exclude = kwargs.get("exclude", ())
        kwargs["exclude"] = tuple([*exclude, "page", "per_page"])
        return super().model_dump(*args, **kwargs)

    async def paginate(self, query: Sized | QuerySet) -> list[Any]:
        """分页"""
        query_iterable: bool = isinstance(query, Sized)  # 判断输出的对象是否可迭代
        page = self.page
        per_page = self.per_page
        if isinstance(query, QuerySet):
            s = (page - 1) * per_page
            items = await query[s: s + per_page].all()
            total = await query.count()
        elif isinstance(query, Sized):
            s = (page - 1) * per_page
            items = query[s: s + per_page]
            total = len(query)
        else:
            raise TypeError(f"bad {query=} for paginating")
        pages = total // per_page
        if total % per_page > 0:
            pages += 1
        self._pagination = Pagination(
            page=page,
            per_page=per_page,
            total=total
        )
        return items

    @property
    def pagination(self) -> Pagination:
        """分页信息"""
        assert self._pagination is not None, f"{self}: please execute paginate first."
        return self._pagination


class RequestKeywordFilterMixin(pdm):
    """模糊搜索指定"""
    keyword: str | None = Field(None, description="模糊查询文本")

    def model_dump(self, *args, **kwargs) -> dict[str, Any]:
        exclude = kwargs.get("exclude", ())
        kwargs["exclude"] = tuple([*exclude, "keyword"])
        return super().model_dump(*args, **kwargs)

    def query_keyword(self, obj: QuerySet | TModel, *args) -> QuerySet:
        """
        查询sql的like语句，模糊匹配
        :param obj: 指定一个已有的查询集，或者指定某个tortoise model也可
        :param args: 需要模糊查询的文本字段
        """
        if isinstance(obj, TModel):
            obj = obj.filter()
        elif isinstance(obj, QuerySet):
            pass
        else:
            assert 0
        if not args or not self.keyword:
            return obj
        to_query = Q()
        for s in args:
            to_query = to_query | Q(**{f"{s}__icontains": self.keyword.strip()})
        return obj.filter(to_query)


class RequestPreferredGetterMixin(pdm):
    """返回字段优选getter"""
    _available_getters: dict[str, Type[Any]]
    preferred_getter: str | None = Field(None, description="期望getter")

    @staticmethod
    def build_getters(gts: list[Type[Any]]) -> dict[str, Type[Any]]:
        """分析给定getters"""
        from .tpdm import TGetter
        getter_flags = {}
        tortoise_model = None
        for gt in gts:
            sf = gt.switch_flag()
            if not safe_issubclass(gt, TGetter):
                raise ValueError(f"{gt} is not subclass of {TGetter}")
            if not sf:
                raise ValueError(f"switch flag undefined: {gt}")
            if sf in getter_flags.keys():
                raise ValueError(f"duplicate getter switch flags: {gt}")
            if tortoise_model and gt._meta["cls"] is not tortoise_model:
                raise ValueError(f"given getters containing different tortoise models: {gts}")
            tortoise_model = gt._meta["cls"]
            getter_flags[sf] = gt
        return getter_flags

    @property
    def getter(self) -> type[pdm]:
        """当前根据判断应当使用的getter"""
        for sf, g in self._available_getters.items():
            if sf == self.preferred_getter:
                return g
        assert 0, f"no getter for preferred getter: {self.preferred_getter} in {self}"

    def model_dump(self, *args, **kwargs) -> dict[str, Any]:
        exclude = kwargs.get("exclude", ())
        kwargs["exclude"] = tuple([*exclude, "preferred_getter"])
        return super().model_dump(*args, **kwargs)


class RequestAtLeastOneMixin(pdm):
    """检查要求至少包含一个过滤条件"""

    @model_validator(mode="after")
    def at_lease_one(self):
        values = list(self.model_dump().values())
        assert any(values), "at least one query is required."
        return self


JsonRespDataType = TypeVar("JsonRespDataType")

class JsonResp(pdm, Generic[JsonRespDataType]):
    """通用json返回结构"""
    msg: str | None = None
    data: JsonRespDataType | None = None


class PaginationJsonResp(JsonResp):
    """包含分页信息的通用json返回结构"""
    pagination: Pagination


def build_query(
        query: dict,
        keyword: bool = False,
        pagination: bool = False,
        at_least_one: bool = False,
        getters: tuple[Type[pdm], ...] | None = None,
        annotated_as: Callable = Query
):
    """创建接口查询参数"""
    bases: list[Type[pdm]] = [RequestQuery]
    if keyword:
        bases.append(RequestKeywordFilterMixin)
    if pagination:
        bases.append(RequestPaginationMixin)
    if at_least_one:
        bases.append(RequestAtLeastOneMixin)
    if getters:
        gts = RequestPreferredGetterMixin.build_getters(getters)
        if len(gts) > 1:
            enums = StrEnum(f"anonymous-url-query-getter-names-enum-{uuid.uuid4().hex}", list(gts.keys()))
            enums.__doc__ = "可选返回数据结构"
            preferred_getters_model = create_model(
                f"anonymous-url-query-preferred-getters-switch-model-{uuid.uuid4().hex}",
                __base__=(RequestPreferredGetterMixin,),
                preferred_getter=(enums, Field(default=getters[0].switch_flag()))
            )
            preferred_getters_model._available_getters = gts
            bases.append(preferred_getters_model)
    r = create_model(
        f"anonymous-url-query-model-{uuid.uuid4().hex}",
        __base__=tuple(bases),
        **query
    )
    return Annotated[r, annotated_as()]


class BaseHeaderToken(pdm):
    """处理token相关逻辑的header字段"""
    authorization: str
    _verified: bool = False

    async def verify(self, *args, **kwargs) -> bool:
        """查询当前token有效性，以此提供当前用户、权限等等逻辑"""
        raise NotImplementedError

    async def acquire(self, *privileges) -> bool:
        """要求权限(且"""
        raise NotImplementedError

    async def has(self, *privileges) -> bool:
        """判断是否有权限(且"""
        try:
            await self.acquire(*privileges)
        except NotImplementedError as e:
            raise e
        except:
            return False
        return True


class CollectAPIRouter(APIRouter):
    """根据文件目录遍历py文件以发现接口函数的router"""

    def __init__(self, *, entry_module: str, **kwargs) -> None:
        """
        """
        super().__init__(**kwargs)
        self.entry_module_split = entry_module.split(".")

    def generate_path(self,
                func: Callable,
                path_postfix: str = None) -> str:
        assert callable(func), f"{func} is not callable"
        api_module_split = [i for i in func.__module__.split(".") if i]
        if api_module_split[-1] == "__init__":
            api_module_split = api_module_split[:-1]
        if self.entry_module_split != api_module_split[:len(self.entry_module_split)]:
            raise ValueError(f"{func} was not placed within configured package: {self.entry_module_split}")
        api_path = api_module_split[len(self.entry_module_split):]
        r = "/".join(api_path)
        if path_postfix:
            assert path_postfix.strip().startswith("/"), f"{path_postfix.strip()} should start with '/'"
            r = r + path_postfix.strip()
        if r and not r.startswith("/"):
            r = f"/{r}"
        return r

    def get(self, path_postfix: str = "", **kwargs):
        def _outer(func):
            p = self.generate_path(func, path_postfix=path_postfix)
            return super(CollectAPIRouter, self).get(p, **kwargs)(func)
        return _outer

    def post(self, path_postfix: str = "", **kwargs):
        def _outer(func):
            p = self.generate_path(func, path_postfix=path_postfix)
            return super(CollectAPIRouter, self).post(p, **kwargs)(func)
        return _outer

    def patch(self, path_postfix: str = "", **kwargs):
        def _outer(func):
            p = self.generate_path(func, path_postfix=path_postfix)
            return super(CollectAPIRouter, self).patch(p, **kwargs)(func)
        return _outer

    def put(self, path_postfix: str = "", **kwargs):
        def _outer(func):
            p = self.generate_path(func, path_postfix=path_postfix)
            return super(CollectAPIRouter, self).put(p, **kwargs)(func)
        return _outer

    def delete(self, path_postfix: str = "", **kwargs):
        def _outer(func):
            p = self.generate_path(func, path_postfix=path_postfix)
            return super(CollectAPIRouter, self).delete(p, **kwargs)(func)
        return _outer


# === some useful http exceptions ===

class HttpError(Exception):
    """http异常"""

    status_code: int = None

    def __init__(self, msg: str = None, data: Any = None):
        self.msg = self.__doc__
        if msg:
            self.msg = f"{self.__doc__}: {msg}"
        self.data = data

    def __str__(self):
        return f"{self.msg}: {self.data}"

    @classmethod
    async def exception_handler(cls, request, exc: Exception):
        msg = getattr(exc, "msg", exc.__doc__)
        if exc.args and isinstance(exc.args[0], str):
            msg = exc.args[0]
        return JSONResponse(
            content=JsonResp(msg=msg, data=getattr(exc, "data", None)).model_dump(),
            status_code=getattr(exc, "status_code", status.HTTP_500_INTERNAL_SERVER_ERROR)
        )


class BadRequest(HttpError):
    """请求错误"""
    status_code = status.HTTP_400_BAD_REQUEST


class Unauthorized(HttpError):
    """权限校验失败"""
    status_code = status.HTTP_401_UNAUTHORIZED


class Forbidden(HttpError):
    """禁止"""
    status_code = status.HTTP_403_FORBIDDEN


class NotFound(HttpError):
    """未找到"""
    status_code = status.HTTP_404_NOT_FOUND


class ServerError(HttpError):
    """内部错误"""
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
