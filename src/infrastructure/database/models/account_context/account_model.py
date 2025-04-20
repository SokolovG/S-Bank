from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base
from src.infrastructure.database.config import MAX_BASIC_LENGTH
from src.infrastructure.database.models.enums import AccountType, Currency

if TYPE_CHECKING:
    from src.infrastructure.database.models import CustomerModel
    from src.infrastructure.database.models.payment_context.balance_model import Balance
    from src.infrastructure.database.models.payment_context.card_model import Card
    from src.infrastructure.database.models.transaction_context.transaction_model import Transaction


class Account(Base):
    __tablename__ = "accounts"

    account_number: Mapped[str] = mapped_column(String(MAX_BASIC_LENGTH), index=True, unique=True)
    account_type: Mapped[AccountType]
    currency: Mapped[Currency]
    balance: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=0)
    iban: Mapped[str] = mapped_column(String(MAX_BASIC_LENGTH), index=True, unique=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_blocked: Mapped[bool] = mapped_column(Boolean, default=False)

    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    customer: Mapped["CustomerModel"] = relationship("CustomerModel", back_populates="accounts")
    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction", foreign_keys="[Transaction.source_account_id]", back_populates="source_account"
    )
    incoming_transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction", foreign_keys="[Transaction.destination_account_id]", back_populates="destination_account"
    )
    cards: Mapped[list["Card"]] = relationship("Card", back_populates="account")
    balances: Mapped[list["Balance"]] = relationship("Balance", back_populates="account")
