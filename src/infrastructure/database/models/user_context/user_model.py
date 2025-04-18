from typing import TYPE_CHECKING
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base
from src.infrastructure.database.constants import MAX_BASIC_LENGTH

if TYPE_CHECKING:
    from src.infrastructure.database.models.account_context.account_model import Account
    from src.infrastructure.database.models.payment_context.card_model import Card

class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(MAX_BASIC_LENGTH), index=True, unique=True)
    email: Mapped[str] = mapped_column(String(MAX_BASIC_LENGTH), index=True, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(MAX_BASIC_LENGTH))

    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    accounts: Mapped[list["Account"]] = relationship("Account", back_populates="user")
    cards: Mapped[list["Card"]] = relationship("Card", back_populates="user")