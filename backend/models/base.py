__all__ = [
    "BaseTModel",
    "SetterMeta",
    "build_meta",
    "build_soft_deletion_meta",
    "SoftDeletionModelMixin",
    "EasyForeignKeyField",
]

from typing import Literal, Any, TypeVar

from tortoise.models import Model
from tortoise.fields import DatetimeField, ForeignKeyField, OnDelete, ForeignKeyRelation, ForeignKeyNullableRelation

from backend.core.tpdm import *
from backend.core.soft_deletion import *


MODEL = TypeVar("MODEL", bound="Model")


class BaseTModel(Model):
    create_time = DatetimeField(auto_now_add=True, db_index=True, description="创建时间")
    update_time = DatetimeField(auto_now=True, db_index=True, description="更新时间")

    class Meta:
        abstract = True

    def __str__(self):
        return f"{super().__str__()}: {self.pk}"


class SetterMeta(TPDMMeta):

    # 排除字段是包含了可能会使用的软删字段。
    exclude = (
        "id", "create_time", "update_time", "existed", "deleted_time")


def build_meta(**kwargs):
    kwargs.setdefault("ordering", ("-create_time",))
    return type("Meta", (), kwargs)


def build_soft_deletion_meta(**kwargs):
    kwargs.setdefault("manager", SoftDeletionManager())
    return build_meta(**kwargs)


def EasyForeignKeyField(
        model_name: str,
        related_name: str | None | Literal[False] = None,
        on_delete: OnDelete = OnDelete.NO_ACTION,
        db_constraint: bool = False,
        null: bool = False,
        **kwargs: Any,
) -> ForeignKeyRelation[MODEL] | ForeignKeyNullableRelation[MODEL]:
    return ForeignKeyField(
        model_name,
        related_name,
        on_delete,
        db_constraint,
        null,
        **kwargs
    )
