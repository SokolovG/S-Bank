from sqlalchemy import (
    ForeignKey,
    Numeric,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy.schema import CheckConstraint

from backend.app.infrastructure.database.base import (
    Base,
    BasicString,
    DescriptionString,
    BoolFalse,
    BoolTrue,
    BasicNullString,
    IndexedUniqueString,
)


class User(Base):
    __tablename__ = 'users'
    # String fields.
    username: Mapped[IndexedUniqueString]
    email: Mapped[IndexedUniqueString]
    hashed_password: Mapped[BasicString]
    # Boolean fields
    is_verified: Mapped[BoolFalse]
    is_active: Mapped[BoolTrue]
    # Relationships.
    profile: Mapped["Profile"] = relationship(
        'Profile',
        back_populates='user',
        uselist=False,
        lazy='joined',
        cascade='all, delete-orphan'
    )
    organizer_profile: Mapped["Organizer"] = relationship(
        'Organizer',
        back_populates='user',
        uselist=False,
        lazy='joined',
        cascade='all, delete-orphan'
    )


class Organizer(Base):
    __tablename__ = 'organizers'
    # Foreign Keys.
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', use_alter=True, ondelete='CASCADE'),
        unique=True
    )
    # Relationships.
    authored_events: Mapped[list["Event"]] = relationship(
        'Event',
        lazy='select',
        back_populates='organizer',
        cascade='all, delete-orphan'
    )
    user: Mapped["User"] = relationship(
        'User',
        lazy='joined',
        back_populates='organizer_profile',
        uselist=False,
        cascade='all, delete-orphan'
    )
    # Boolean fields.
    verified: Mapped[BoolFalse]
    # String fields.
    website: Mapped[BasicNullString]
    contact: Mapped[BasicNullString]
    name: Mapped[BasicString]
    description: Mapped[DescriptionString]
    logo_url: Mapped[BasicString] = mapped_column(unique=True)
    # Numeric fields
    rating: Mapped[float] = mapped_column(
        Numeric(3, 2),
        CheckConstraint('rating >= 0 AND rating <= 5'),
        default=0
    )



class Profile(Base):
    __tablename__ = 'profiles'
    # Foreign Keys.
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', use_alter=True, ondelete='CASCADE'),
        unique=True
    )
    # Relationships.
    user: Mapped["User"] = relationship(
        "User",
        back_populates="profile",
        lazy='joined',
        uselist=False,
    )
    registered_events: Mapped[list["Event"]] = relationship(
        "Event",
        secondary='event_registrations',
        back_populates='registered_profiles'
    )
    # Boolean fields.
    notifications_enabled: Mapped[BoolTrue]
    # String fields.
    first_name: Mapped[BasicString]
    last_name: Mapped[BasicString]
    avatar_url: Mapped[BasicNullString]
    interested_technologies: Mapped[BasicNullString]
    location:  Mapped[BasicNullString]
