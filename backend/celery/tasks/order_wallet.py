from decimal import Decimal

from loguru import logger

from backend.celery.task import (
    BaseCeleryTask,
    register_celery_task,
    ScheduledJobTrigger,
    ScheduledJobTriggerArgsInterval,
)
from backend.models import Order, OrderStatus
from backend.services import WalletAccountService
from backend.core.http import Forbidden
from utils import dt_utils


@register_celery_task
class OrderWalletChargeTask(BaseCeleryTask):
    """定时为订单执行预充值钱包扣费"""

    task_type = "order_wallet_charge"

    # 每分钟跑一次，实际可按需调整
    SCHEDULED_JOB_TRIGGER = ScheduledJobTrigger.interval.value
    SCHEDULED_JOB_TRIGGER_ARGS = ScheduledJobTriggerArgsInterval(minutes=1)

    @classmethod
    async def task(cls, task_record_id: int | None = None, **kwargs):
        # 扣费目标：所有状态为「进行中」且到期（order_date <= today）的订单
        today = dt_utils.dt_now().date()
        orders = await Order.filter(status=OrderStatus.processing.value, order_date__lte=today)
        logger.info(f"OrderWalletChargeTask: found {len(orders)} due processing orders to handle (today={today}).")

        for o in orders:
            # 这里约定使用 order_guanxi_id 作为钱包账户标识
            customer_code = (getattr(o, "customer_code", None) or "").strip() or str(o.order_guanxi_id)
            amount = Decimal(o.total_price)
            if amount <= 0:
                o.status = OrderStatus.paid.value
                await o.save()
                continue

            try:
                await WalletAccountService.consume(
                    customer_code=customer_code,
                    amount=amount,
                    related_order_id=o.order_id,
                    remark="订单定时扣费",
                )
                o.status = OrderStatus.paid.value
                await o.save()
                logger.info(f"order {o.order_id} charged successfully from wallet {customer_code}.")
            except Forbidden:
                # 余额不足等情况，标记为支付失败，等待人工处理或再次充值后重试
                o.status = OrderStatus.pay_failed.value
                await o.save()
                logger.warning(f"order {o.order_id} charge failed (wallet={customer_code}), marked as pay_failed.")

