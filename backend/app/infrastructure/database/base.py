from datetime import datetime
from typing import Annotated

from sqlalchemy import Boolean, Integer, String, func
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)

from backend.app.constants import (
    MAX_BASIC_LENGTH,
    MAX_DESCRIPTION_LENGTH,
)


class Base(DeclarativeBase):
    """Base class for models.

    Contains for all models
    - id
    - created_at
    """

    __abstract__ = True
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())


# Basic string with max_length limit.
BasicString = Annotated[str, mapped_column(String(length=MAX_BASIC_LENGTH))]
# Basic string with max_length limit and nullable=True.
BasicNullString = Annotated[str, mapped_column(String(length=MAX_BASIC_LENGTH), nullable=True)]
# Indexed string with max_length limit.
IndexedString = Annotated[str, mapped_column(String(length=MAX_BASIC_LENGTH), index=True)]
# Indexed string with max_length limit und unique=True.
IndexedUniqueString = Annotated[
    str,
    mapped_column(String(length=MAX_BASIC_LENGTH), index=True, unique=True)
]
# Basic string for description with max_length limit.
DescriptionString = Annotated[str, mapped_column(String(length=MAX_DESCRIPTION_LENGTH))]
# Basic bool var, default=False.
BoolFalse = Annotated[bool, mapped_column(Boolean, default=False)]
# Basic bool var, default=True.
BoolTrue = Annotated[bool, mapped_column(Boolean, default=True)]
# Basic integer var with nullable=True.
BasicNullInteger = Annotated[int, mapped_column(Integer, nullable=True)]
