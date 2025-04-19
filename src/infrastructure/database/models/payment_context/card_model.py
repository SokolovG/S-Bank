from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base
from src.infrastructure.database.config import MAX_BASIC_LENGTH
from src.infrastructure.database.models.enums import CardType

if TYPE_CHECKING:
    from src.infrastructure.database.models.account_context.account_model import Account
    from src.infrastructure.database.models.user_context.user_model import UserModel


class Card(Base):
    """Model of bank card."""

    __tablename__ = "cards"

    card_number: Mapped[str] = mapped_column(String(MAX_BASIC_LENGTH), index=True, unique=True)
    card_type: Mapped[CardType]
    exp_date: Mapped[date]
    cvv_hash: Mapped[str] = mapped_column(String(MAX_BASIC_LENGTH))
    is_activated: Mapped[bool] = mapped_column(Boolean, default=False)
    is_blocked: Mapped[bool] = mapped_column(Boolean, default=False)

    daily_limit: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    user: Mapped["UserModel"] = relationship("User", back_populates="cards")
    account: Mapped["Account"] = relationship("Account", back_populates="cards")
