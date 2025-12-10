__all__ = [
    "Privilege",
    "PrivilegeGroup",
    "PrivilegeSet"
]

import uuid
from typing import Self, Union

from pydantic import BaseModel, Field


class Privilege(BaseModel):
    """一个权限"""
    id: str | None = Field(default=None, description="用于前端区分的临时id")
    name: str = Field(default=None, description="权限唯一编号")
    title: str = Field(description="权限名")
    description: str | None = Field(default=None, description="权限额外描述信息")


class PrivilegeGroup(BaseModel):
    """权限组"""
    id: str = Field(default_factory=lambda: uuid.uuid4().hex, description="用于前端区分的临时id")
    title: str = Field(description="组名")
    children: list[Union[Privilege, "PrivilegeGroup"]] = Field(default_factory=list)


class PrivilegeSetMeta(type):

    def __init__(cls, name, bases, attrs: dict):
        super().__init__(name, bases, attrs)

        # 全部的privilege dict
        cls.ALL_PRIVILEGE_DICT: dict[str, Privilege] = {}

        for a_name, p in attrs.items():
            if isinstance(p, Privilege):
                if a_name in cls.ALL_PRIVILEGE_DICT:
                    raise ValueError(f"duplicated privilege name: {a_name}")
                if not p.name:
                    p.name = a_name
                cls.ALL_PRIVILEGE_DICT[a_name] = p


class PrivilegeSet(metaclass=PrivilegeSetMeta):
    """权限集"""

    @classmethod
    def all(cls) -> list[Privilege]:
        return list(cls.ALL_PRIVILEGE_DICT.values())

    @classmethod
    def all_names(cls) -> list[str]:
        return list(cls.ALL_PRIVILEGE_DICT.keys())

    @classmethod
    def get(cls, v: str | Privilege | None) -> Privilege | None:
        if isinstance(v, Privilege):
            return v
        return cls.ALL_PRIVILEGE_DICT.get(v, None)
