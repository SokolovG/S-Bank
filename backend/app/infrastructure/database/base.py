from datetime import datetime
from typing import Annotated, Protocol, ClassVar, Final

from sqlalchemy import Boolean, Integer, String, func, MetaData
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)

from backend.app.core.constants import (
    MAX_BASIC_LENGTH,
    MAX_DESCRIPTION_LENGTH,
)


class BaseModel(DeclarativeBase):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )


class Base(BaseModel):
    """Base class for models.

    Contains for all models
    - [[[[id]]]]
    - created_at
    """

    __abstract__ = True
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())


class SQLAlchemyModel(Protocol):
    __tablename__ = ClassVar[str]


# Basic string with max_length limit.
BasicString = Final[Annotated[str, mapped_column(String(length=MAX_BASIC_LENGTH))]]
# Basic string with max_length limit and nullable=True.
BasicNullString = Final[
    Annotated[str, mapped_column(String(length=MAX_BASIC_LENGTH), nullable=True)]
]
# Indexed string with max_length limit.
IndexedString = Final[
    Annotated[str, mapped_column(String(length=MAX_BASIC_LENGTH), index=True)]
]
# Indexed string with max_length limit und unique=True.
IndexedUniqueString = Final[
    Annotated[
        str, mapped_column(String(length=MAX_BASIC_LENGTH), index=True, unique=True)
    ]
]
# Basic string for description with max_length limit.
DescriptionString = Final[
    Annotated[str, mapped_column(String(length=MAX_DESCRIPTION_LENGTH))]
]
# Basic bool var, default=False.
BoolFalse = Final[Annotated[bool, mapped_column(Boolean, default=False)]]
# Basic bool var, default=True.
BoolTrue = Final[Annotated[bool, mapped_column(Boolean, default=True)]]
# Basic integer var with nullable=True.
BasicNullInteger = Final[Annotated[int, mapped_column(Integer, nullable=True)]]
