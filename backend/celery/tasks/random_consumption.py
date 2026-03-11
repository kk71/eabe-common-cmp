from __future__ import annotations

import random
from decimal import Decimal
from datetime import timedelta

from loguru import logger

from backend.celery.task import (
    BaseCeleryTask,
    register_celery_task,
    ScheduledJobTrigger,
    ScheduledJobTriggerArgsInterval,
)
from backend.core.http import Forbidden
from backend.models import RandomConsumptionRule, WalletTransaction, WalletTransactionType
from backend.services import WalletAccountService
from utils import dt_utils


def _rand_decimal(min_v: Decimal, max_v: Decimal) -> Decimal:
    if max_v < min_v:
        min_v, max_v = max_v, min_v
    if max_v == min_v:
        return min_v.quantize(Decimal("0.01"))
    cents_min = int((min_v * 100).to_integral_value())
    cents_max = int((max_v * 100).to_integral_value())
    return Decimal(random.randint(cents_min, cents_max)) / Decimal(100)


@register_celery_task
class RandomConsumptionGenerateTask(BaseCeleryTask):
    """定时按规则随机生成消费记录（token/短信/流量费等）"""

    task_type = "random_consumption_generate"

    # 每分钟跑一次；每条规则内部再做 interval_minutes 限频
    SCHEDULED_JOB_TRIGGER = ScheduledJobTrigger.interval.value
    SCHEDULED_JOB_TRIGGER_ARGS = ScheduledJobTriggerArgsInterval(minutes=1)

    @classmethod
    async def task(cls, task_record_id: int | None = None, **kwargs):
        now = dt_utils.dt_now()
        rules = await RandomConsumptionRule.filter(enabled=True)
        if not rules:
            return

        for r in rules:
            # 简单限频：过去 interval_minutes 内是否已生成过该规则的消费流水
            minutes = int(r.interval_minutes or 60)
            since = now - timedelta(minutes=minutes)

            recent = await WalletTransaction.filter(
                tx_type=WalletTransactionType.consume.value,
                wallet__customer_code=r.customer_code,
                remark__contains=f"[RANDOM:{r.id}]",
                create_time__gte=since,
            ).first()
            if recent:
                continue

            amount = _rand_decimal(Decimal(str(r.min_amount or 0)), Decimal(str(r.max_amount or 0)))
            if amount <= 0:
                continue

            try:
                await WalletAccountService.consume(
                    customer_code=r.customer_code,
                    amount=amount,
                    remark=f"[RANDOM:{r.id}] {r.product_type} 随机消费",
                    related_bill_id=None,
                )
                logger.info(f"RandomConsumptionGenerateTask: generated consume {amount} for {r.customer_code} ({r.product_type}).")
            except Forbidden:
                # 余额不足等，直接跳过
                continue

