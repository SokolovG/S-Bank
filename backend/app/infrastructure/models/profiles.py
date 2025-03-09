from typing import TYPE_CHECKING
from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.infrastructure.database.base import (
    Base,
    BasicNullString,
    BasicString,
    BoolTrue,
)
from backend.app.infrastructure.models.enums import Gender

if TYPE_CHECKING:
    from .users import User
    from .events import Event


class Profile(Base):
    """Regular user profile model.

    Contains additional information about regular users.
    """

    __tablename__ = "profiles"

    # Foreign Keys
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", use_alter=True, ondelete="CASCADE"), unique=True
    )

    # Relationships
    user: Mapped["User"] = relationship(
        "User",
        back_populates="profile",
        lazy="joined",
        uselist=False,
    )
    registered_events: Mapped[list["Event"]] = relationship(
        "Event",
        secondary="event_registrations",
        back_populates="registered_profiles",
        lazy="selectin",
    )

    # Boolean fields
    notifications_enabled: Mapped[BoolTrue]

    # String fields
    first_name: Mapped[BasicString]
    last_name: Mapped[BasicString]
    avatar_url: Mapped[BasicNullString]
    interested_technologies: Mapped[BasicNullString]
    location: Mapped[BasicNullString]
    birth_date: Mapped[date]
    gender: Mapped[Gender] = mapped_column(nullable=True)
