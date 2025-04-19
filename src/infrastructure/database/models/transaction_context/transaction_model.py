from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base
from src.infrastructure.database.config import MAX_BASIC_LENGTH, MAX_DESCRIPTION_LENGTH
from src.infrastructure.database.models.enums import Currency, TransactionStatus, TransactionType

if TYPE_CHECKING:
    from src.infrastructure.database.models.account_context.account_model import Account


class Transaction(Base):
    __tablename__ = "transactions"

    transaction_type: Mapped[TransactionType]
    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    currency: Mapped[Currency]
    status: Mapped[TransactionStatus]
    description: Mapped[str] = mapped_column(String(MAX_DESCRIPTION_LENGTH))

    source_account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    destination_account_id: Mapped[int | None] = mapped_column(ForeignKey("accounts.id"), nullable=True)

    recipient_name: Mapped[str | None] = mapped_column(String(MAX_BASIC_LENGTH), nullable=True)
    recipient_iban: Mapped[str | None] = mapped_column(String(MAX_BASIC_LENGTH), nullable=True)
    swift_code: Mapped[str | None] = mapped_column(String(MAX_BASIC_LENGTH), nullable=True)

    transaction_date: Mapped[datetime] = mapped_column(default=func.now())
    processed_date: Mapped[datetime]

    source_account: Mapped["Account"] = relationship(
        "Account", foreign_keys=[source_account_id], back_populates="transactions"
    )
    destination_account: Mapped["Account | None"] = relationship(
        "Account", foreign_keys=[destination_account_id], back_populates="incoming_transactions"
    )
