__all__ = [
    "WalletAccountService",
]

from decimal import Decimal
from typing import Optional

from tortoise.transactions import in_transaction

from backend.core.http import Forbidden, NotFound
from backend.models import WalletAccount, WalletTransaction, WalletTransactionType


class WalletAccountService:
    """预充值钱包账户服务"""

    @staticmethod
    def _ensure_decimal(v) -> Decimal:
        if isinstance(v, Decimal):
            return v
        if v is None:
            return Decimal("0.00")
        return Decimal(str(v))

    @classmethod
    async def get_or_create_account(cls, customer_code: str, customer_name: Optional[str] = None) -> WalletAccount:
        w = await WalletAccount.filter(customer_code=customer_code).first()
        if w:
            # 更新一下名称，避免老数据名称过期
            if customer_name and w.customer_name != customer_name:
                w.customer_name = customer_name
                await w.save()
            return w
        return await WalletAccount.create(
            customer_code=customer_code,
            customer_name=customer_name,
        )

    @classmethod
    async def recharge(
        cls,
        customer_code: str,
        amount: Decimal,
        remark: str | None = None,
        customer_name: Optional[str] = None,
    ) -> WalletAccount:
        """充值入账"""
        amount = cls._ensure_decimal(amount)
        if amount <= 0:
            raise Forbidden("充值金额必须大于0")

        async with in_transaction():
            wallet = await cls.get_or_create_account(customer_code, customer_name=customer_name)
            wallet.balance = cls._ensure_decimal(wallet.balance)
            wallet.total_recharge = cls._ensure_decimal(wallet.total_recharge)
            wallet.balance += amount
            wallet.total_recharge += amount
            await wallet.save()
            await WalletTransaction.create(
                wallet=wallet,
                tx_type=WalletTransactionType.recharge.value,
                change_amount=amount,
                balance_after=wallet.balance,
                remark=remark,
            )
            return wallet

    @classmethod
    async def consume(
        cls,
        customer_code: str,
        amount: Decimal,
        remark: str | None = None,
        related_order_id: str | None = None,
        related_bill_id: str | None = None,
    ) -> WalletAccount:
        """消费扣费"""
        if amount <= 0:
            raise Forbidden("消费金额必须大于0")

        async with in_transaction():
            wallet = await WalletAccount.filter(customer_code=customer_code).first()
            if not wallet:
                raise NotFound("钱包账户不存在")
            if wallet.balance < amount:
                raise Forbidden("余额不足")
            wallet.balance -= amount
            await wallet.save()
            await WalletTransaction.create(
                wallet=wallet,
                tx_type=WalletTransactionType.consume.value,
                change_amount=-amount,
                balance_after=wallet.balance,
                related_order_id=related_order_id,
                related_bill_id=related_bill_id,
                remark=remark,
            )
            return wallet

