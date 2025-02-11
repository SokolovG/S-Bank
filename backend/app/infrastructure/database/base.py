from typing import Annotated
from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, func, String, Boolean

from backend.app.constants import MAX_BASIC_LENGTH, MAX_DESCRIPTION_LENGTH

class Base(DeclarativeBase):
    """Base class for models."""
    __abstract__ = True
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())


BasicString = Annotated[str, mapped_column(String(length=MAX_BASIC_LENGTH))]
BasicNullString = Annotated[str, mapped_column(String(length=MAX_BASIC_LENGTH), nullable=True)]
IndexedString = Annotated[str, mapped_column(String(length=MAX_BASIC_LENGTH), index=True)]
IndexedUniqueString = Annotated[str, mapped_column(String(length=MAX_BASIC_LENGTH), index=True, unique=True)]
DescriptionString = Annotated[str, mapped_column(String(length=MAX_DESCRIPTION_LENGTH))]
BoolFalse = Annotated[bool, mapped_column(Boolean, default=False)]
BoolTrue = Annotated[bool, mapped_column(Boolean, default=True)]
BasicNullInteger = Annotated[int, mapped_column(Integer, nullable=True)]