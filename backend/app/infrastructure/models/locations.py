from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from backend.app.infrastructure.database.base import (
    Base,
    BasicString,
    IndexedString,
)
if TYPE_CHECKING:
    from .events import Event


class Location(Base):
    """Model for event locations.

    Represents physical locations where events can take place.
    """

    __tablename__ = 'locations'

    # String fields
    name: Mapped[BasicString]
    address: Mapped[BasicString]
    city: Mapped[IndexedString]
    country: Mapped[IndexedString]

    # Relationships
    events: Mapped["Event"] = relationship(
        'Event',
        back_populates='location',
        cascade='all, delete-orphan'
    )
