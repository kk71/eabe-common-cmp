__all__ = [
    "SoftDeletionModelMixin",
    "SoftDeletionManager",
    "SoftDeletionQuerySet",
]

from typing import Iterable

import arrow
from loguru import logger
from tortoise.manager import Manager
from tortoise import Model, BaseDBAsyncClient
from tortoise.fields import BooleanField, DatetimeField
from tortoise.queryset import QuerySet, UpdateQuery


class SoftDeletionQuerySet(QuerySet):

    def delete(self) -> UpdateQuery:
        """
        偷梁换柱，把删除查询集变成更新查询集中数据为已删除
        """
        return super().update(
            existed=None,
            deleted_time=arrow.now().replace(tzinfo=None).shift(hours=8).datetime
        )


class SoftDeletionManager(Manager):

    def get_queryset(self):
        return SoftDeletionQuerySet(self._model).filter(existed=True)


class SoftDeletionModelMixin:
    """支持可配置软删的tortoise model mixin"""
    existed = BooleanField(default=True, null=True, db_index=True, description="数据是否存在")
    deleted_time = DatetimeField(null=True, db_index=True, description="软删时间")
    
    class Meta:
        abstract = True

    async def delete(self, using_db: BaseDBAsyncClient | None = None) -> None:
        if not self.existed:
            logger.warning(f"record has been soft-deleted and is still trying to be deleted again: {self}")
        if self.existed:
            self.deleted_time = arrow.now().replace(tzinfo=None).shift(hours=8).datetime
            self.existed = None
            return await super().save(using_db=using_db, update_fields=("existed", "deleted_time"))

    async def save(
        self,
        using_db: BaseDBAsyncClient | None = None,
        update_fields: Iterable[str] | None = None,
        force_create: bool = False,
        force_update: bool = False,
    ) -> None:
        if not self.existed:
            logger.warning(f"record has been soft-deleted and is still trying to be saved: {self}")
        return await super().save(using_db, update_fields, force_create, force_update)
