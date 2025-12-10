__all__ = [
    "TGetter",
    "TSetter",
    "TPDMMeta",
    "init_t_pdm",
]

from typing import Any, Type

from loguru import logger
from tortoise.models import Model as tm
from tortoise.fields.relational import RelationalField
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel as pdm, create_model, ConfigDict

from .cls_utils import *


# 存放全部的getter自动切换标志，用于防止重复
switch_flags: set[str] = set()


class BaseTPDM(pdm):

    model_config = ConfigDict(
        extra="ignore",
        coerce_numbers_to_str=True,
    )

    # 以下参数需要在初始化的时候被填充
    _meta: dict[str, Any]

    @classmethod
    def check_if_initialized(cls):
        if cls._meta and isinstance(cls._meta, dict) and cls._meta.get("cls"):
            return
        raise NotImplementedError(f"{cls}: Base tortoise-based pydantic model can't be used directly."
                                  f"You need initialize it first.")

    @classmethod
    def integrity_check(cls):
        """一致性检查"""

    @classmethod
    def judge_exclude(cls, tm_cls: Type[tm]) -> tuple[str, ...]:
        """
        判断某个tortoise model class包含哪些需要被排除的特殊字段（外键之类的）
        本方法在init_t_pdm中调用
        :param tm_cls:
        """
        assert safe_issubclass(tm_cls, tm), f"{tm_cls} is not a subclass of {tm}"
        return tuple([
            k
            for k, v in tm_cls._meta.fields_map.items()
            if isinstance(v, RelationalField)
        ])

    def json_schema_title(self) -> str:
        r = [
            self._meta['cls'].__name__,
            self.__name__
        ]
        return r.pop(0) + f"({', '.join(r)})"


class TGetter(BaseTPDM):

    @classmethod
    def switch_flag(cls) -> str | None:
        """用于自动切换的标志"""

    def json_schema_title(self) -> str:
        r = [
            self._meta['cls'].__name__,
            self.__name__
        ]
        if sf := self.switch_flag():
            r.append(f"switch_flag={sf}")
        return r.pop(0) + f"({', '.join(r)})"

    @classmethod
    async def extra_fields(cls, t_inst: tm, results: dict[str, Any]) -> None:
        """
        输出非TModel的字段
        :param t_inst: tortoise model实例
        :param results: 字段值放入此字典
        """

    @classmethod
    async def parse_record(cls, t_inst: tm, **kwargs) -> "TGetter":
        """从对应的tortoise实例创建getter"""
        cls.check_if_initialized()

        # begin:TODO 下述代码从tortoise.contrib.pydantic.base迁移，需要注意tortoise迭代是否会影响
        from tortoise.contrib.pydantic.base import _get_fetch_fields
        # Get fields needed to fetch
        fetch_fields = _get_fetch_fields(cls, cls.model_config["orig_model"])  # type: ignore
        # Fetch fields
        await t_inst.fetch_related(*fetch_fields)
        # end:

        model_kv = {}
        for k, f in cls.model_config["orig_model"]._meta.fields_map.items():
            if isinstance(f, RelationalField):
                continue
            model_kv[k] = getattr(t_inst, k)
        await cls.extra_fields(t_inst, extra_kv := {})
        to_validate = {**model_kv, **extra_kv}
        return cls.model_validate(to_validate, **kwargs)

    @classmethod
    def integrity_check(cls):
        switch_flag = cls.switch_flag
        if isinstance(switch_flag, str):
            if " " in switch_flag or not len(switch_flag):
                raise ValueError(f"bad switch flag for getter: {cls}")
            if switch_flag in switch_flags:
                raise ValueError(f"duplicated switch flag for getter: {switch_flag}")
            switch_flags.add(switch_flag)


class TSetter(BaseTPDM):

    async def write_record(self,
                           t_inst: tm,
                           process_save: bool = True,
                           **kwargs):
        """
        执行写入tortoise记录操作
        :param t_inst:
        :param process_save: 是否执行保存操作
        :param kwargs 额外参数传给t_inst.save方法
        """
        self.check_if_initialized()
        if not isinstance(t_inst, self._meta["cls"]):
            raise TypeError(f"{t_inst=} is not an instance of {self._meta["cls"]}")
        for k, v in self._meta["cls"]._meta.fields_map.items():
            if isinstance(v, RelationalField):
                continue
            if not hasattr(self, k):
                continue
            setattr(t_inst, k, getattr(self, k))
        await self.before_saving(t_inst)
        if process_save:
            await t_inst.save(**kwargs)
            await self.after_saving(t_inst)

    async def before_saving(self, t_inst: tm):
        """tortoise model字段已更新，但是在写入数据库之前执行"""

    async def after_saving(self, t_inst: tm):
        """tortoise model字段已更新且保存，然后再执行"""


class TPDMMetaMeta(type):

    def __init__(cls, name, bases, attrs: dict):
        super().__init__(name, bases, attrs)
        if not bases:
            return
        base = bases[-1]
        attrs_populated = {}
        for k in dir(base):
            if k.startswith("_"):
                continue
            attrs_populated[k] = getattr(base, k)
        for k, v in attrs.items():
            if isinstance(v, (tuple, list)):
                parent = getattr(base, k, None)
                assert isinstance(parent, tuple | list | None)
                if "include" in k.lower():
                    if parent is None:
                        attrs_populated[k] = list(v)
                    else:
                        # 列表的包含逻辑：即子类囊括的值必须是父类的子集
                        assert set(v).issubset(parent)
                        attrs_populated[k] = list(v)
                elif "exclude" in k.lower():
                    if parent is None:
                        attrs_populated[k] = list(set(v))
                    else:
                        # 列表的去除逻辑：即子类囊括的值是父类的值于子类配置的值的并集
                        attrs_populated[k] = list(set(list(parent) + list(v)))
        for k, v in attrs_populated.items():
            setattr(cls, k, v)


class TPDMMeta(metaclass=TPDMMetaMeta):
    """便于构造针对include和exclude字段进行继承的meta"""
    pass


def extract_meta(cls) -> dict:
    t_meta = getattr(cls, "TMeta", None)
    if not t_meta:
        raise NotImplementedError(f"no TMeta implemented for {cls}")
    mappings = {}
    for k in dir(t_meta):
        if k.startswith("_"):
            continue
        mappings[k] = getattr(t_meta, k)
    return mappings


def init_t_pdm(cls):
    """初始化为一个tortoise-orm对应的getter或者setter"""
    mappings = extract_meta(cls)
    if safe_issubclass(cls, TGetter):
        class MetaOverride:
            exclude = TGetter.judge_exclude(mappings["cls"])
            backward_relations = False
            exclude_raw_fields = False
    elif safe_issubclass(cls, TSetter):
        class MetaOverride:
            exclude = TSetter.judge_exclude(mappings["cls"])
            backward_relations = False
            exclude_raw_fields = False
    else:
        raise TypeError(f"{cls} must be subclass of {BaseTPDM}.")
    mappings["meta_override"] = MetaOverride
    original_t_pdm = pydantic_model_creator(**mappings)
    r = create_model(
        cls.__name__,
        __base__=(cls, original_t_pdm),  # TODO 注意这里的顺序不确定会不会出问题
        __doc__=cls.__doc__,
        __module__=cls.__module__,
        __config__=BaseTPDM.model_config
    )
    r._meta = mappings
    r.model_config["title"] = None
    r.model_config["model_title_generator"] = getattr(r, "json_schema_title")
    r.integrity_check()
    return r
