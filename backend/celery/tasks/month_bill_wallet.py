from __future__ import annotations

from decimal import Decimal
from collections import defaultdict

from loguru import logger

from backend.celery.task import (
    BaseCeleryTask,
    register_celery_task,
    ScheduledJobTrigger,
    ScheduledJobTriggerArgsCron,
)
from backend.core.http import Forbidden
from backend.models import MonthBill, MonthBillChargeRecord, MonthBillChargeStatus, WalletTransaction
from backend.services import WalletAccountService
from utils import dt_utils


def _bill_key(year: int, month: int, customer_code: str) -> str:
    return f"{year:04d}{month:02d}:{customer_code}"


@register_celery_task
class MonthBillWalletChargeTask(BaseCeleryTask):
    """定时对“月度账单”按客户+年月汇总扣费（生成钱包消费流水）"""

    task_type = "month_bill_wallet_charge"

    # 每天凌晨 02:10 跑一次，扣“上一个自然月”的账单
    SCHEDULED_JOB_TRIGGER = ScheduledJobTrigger.cron.value
    SCHEDULED_JOB_TRIGGER_ARGS = ScheduledJobTriggerArgsCron(hour=2, minute=10, second=0)

    @classmethod
    async def task(cls, task_record_id: int | None = None, **kwargs):
        now = dt_utils.dt_now()
        year = now.year
        month = now.month - 1
        if month == 0:
            month = 12
            year -= 1

        bills = await MonthBill.filter(year=year, month=month)
        if not bills:
            logger.info(f"MonthBillWalletChargeTask: no bills for {year}-{month:02d}.")
            return

        grouped_amount: dict[tuple[str, str | None], Decimal] = defaultdict(lambda: Decimal("0.00"))
        for b in bills:
            customer_code = b.customer_code
            grouped_amount[(customer_code, b.customer_name)] += Decimal(str(b.total_paid or 0))

        logger.info(f"MonthBillWalletChargeTask: {len(grouped_amount)} customers to charge for {year}-{month:02d}.")

        for (customer_code, customer_name), total in grouped_amount.items():
            total = Decimal(total).quantize(Decimal("0.01"))
            if total <= 0:
                continue

            bk = _bill_key(year, month, customer_code)
            existing = await MonthBillChargeRecord.filter(bill_key=bk).first()
            if existing and existing.status == MonthBillChargeStatus.charged.value:
                continue

            record = existing
            if not record:
                record = await MonthBillChargeRecord.create(
                    year=year,
                    month=month,
                    customer_code=customer_code,
                    customer_name=customer_name,
                    bill_key=bk,
                    total_amount=total,
                    status=MonthBillChargeStatus.pending.value,
                    related_bill_id=bk,
                )
            else:
                # 若已存在但未成功，允许重试：刷新金额、清空错误
                record.total_amount = total
                record.customer_name = customer_name
                record.status = MonthBillChargeStatus.pending.value
                record.error_info = None
                if not record.related_bill_id:
                    record.related_bill_id = bk
                await record.save()

            try:
                wallet = await WalletAccountService.consume(
                    customer_code=customer_code,
                    amount=total,
                    related_bill_id=record.related_bill_id,
                    remark=f"月账单扣费 {year}-{month:02d}",
                )
                # 通过 related_bill_id 找到刚写入的流水（弱关联，足够用于展示/追溯）
                tx = await WalletTransaction.filter(
                    wallet_id=wallet.id,
                    related_bill_id=record.related_bill_id,
                ).order_by("-id").first()
                record.status = MonthBillChargeStatus.charged.value
                record.wallet_tx_id = tx.tx_id if tx else None
                await record.save()
            except Forbidden as e:
                record.status = MonthBillChargeStatus.failed.value
                record.error_info = str(e)
                await record.save()
            except Exception as e:
                record.status = MonthBillChargeStatus.failed.value
                record.error_info = str(e)[:2000]
                await record.save()

