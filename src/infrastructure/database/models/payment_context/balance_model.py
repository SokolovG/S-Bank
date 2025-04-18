from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base

if TYPE_CHECKING:
    from src.infrastructure.database.models.account_context.account_model import Account


class Balance(Base):
    __tablename__ = "balances"

    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), primary_key=True)
    balance_type: Mapped[str] = mapped_column(primary_key=True)  # "available", "pending", "reserved"
    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=0)

    account: Mapped["Account"] = relationship("Account", back_populates="balances")