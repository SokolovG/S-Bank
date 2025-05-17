from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base
from src.infrastructure.database.config import MAX_BASIC_LENGTH


class UserModel(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(MAX_BASIC_LENGTH), index=True, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(MAX_BASIC_LENGTH))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    blocked: Mapped[bool] = mapped_column(Boolean, default=False)
    reason_for_blocking: Mapped[str] = mapped_column(String(MAX_BASIC_LENGTH), nullable=True)

    customer = relationship("CustomerModel", uselist=False, back_populates="user")
