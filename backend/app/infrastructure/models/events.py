"""Models for events, locations, and categories management."""
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.infrastructure.database.base import (
    Base,
    BasicNullInteger,
    BasicNullString,
    BasicString,
    BoolFalse,
    DescriptionString,
    IndexedString,
    IndexedUniqueString,
)
from backend.app.infrastructure.models.enums import (
    Currency,
    EventFormat,
    EventStatus,
)

if TYPE_CHECKING:
    from .users import Organizer, Profile


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


class Category(Base):
    """Model for event categories.

    Represents different types/categories of events.
    """

    __tablename__ = 'categories'

    # String fields
    name: Mapped[BasicString]
    slug: Mapped[IndexedUniqueString]
    description: Mapped[DescriptionString]

    # Relationships
    events = relationship('Event', back_populates='category')


class Event(Base):
    """Model for events.

    Main event model containing all event-related information.
    """

    __tablename__ = 'events'

    # Basic fields
    name: Mapped[IndexedString]
    description: Mapped[DescriptionString]

    # Foreign Keys
    organizer_id: Mapped[int] = mapped_column(
        ForeignKey('organizers.id', use_alter=True))
    location_id: Mapped[int] = mapped_column(
        ForeignKey('locations.id', use_alter=True),
        nullable=True
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey('categories.id', use_alter=True),
    )

    # Relationships
    organizers: Mapped[list["Organizer"]] = relationship(
        'Organizer',
        secondary='event_organizers',
        back_populates='events',
        lazy='select'
    )
    location: Mapped["Location"] = relationship(
        'Location',
        back_populates='events'
    )
    category: Mapped["Category"] = relationship(
        'Category',
        back_populates='events'
    )
    registered_profiles: Mapped[list["Profile"]] = relationship(
        "Profile",
        secondary='event_registrations',
        back_populates='registered_events'
    )

    # Enum fields
    format: Mapped[EventFormat] = mapped_column(
        default=EventFormat.OFFLINE,
    )
    status: Mapped[EventStatus] = mapped_column(
        default=EventStatus.PLANNED
    )
    currency: Mapped[Currency] = mapped_column(
        default=Currency.USD,
    )

    # Boolean fields
    is_published: Mapped[BoolFalse]
    is_online: Mapped[BoolFalse]
    is_verify: Mapped[BoolFalse]

    # Date fields
    pub_date: Mapped[DateTime]
    event_start_date: Mapped[DateTime]
    event_end_date: Mapped[DateTime]
    registration_deadline: Mapped[DateTime] = mapped_column(nullable=True)

    # String fields
    meeting_link: Mapped[BasicNullString]
    timezone: Mapped[BasicString] = mapped_column(default='UTC')

    # Numeric fields
    max_participants: Mapped[BasicNullInteger]
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=True)
    current_participants: Mapped[BasicNullInteger]
