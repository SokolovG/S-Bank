from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base
from src.infrastructure.database.config import MAX_BASIC_LENGTH

if TYPE_CHECKING:
    from src.infrastructure.database.models.account_context.account_model import Account


class CustomerModel(Base):
    __tablename__ = "customers"

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), unique=True)

    username: Mapped[str] = mapped_column(String(MAX_BASIC_LENGTH), index=True, unique=True)
    first_name: Mapped[str] = mapped_column(String(MAX_BASIC_LENGTH))
    last_name: Mapped[str] = mapped_column(String(MAX_BASIC_LENGTH), index=True)
    birth_date: Mapped[datetime]

    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)

    phone: Mapped[str] = mapped_column(String(MAX_BASIC_LENGTH), index=True, unique=True)
    accounts: Mapped[list["Account"]] = relationship("Account", back_populates="customer")

    user = relationship("UserModel", back_populates="customer")
