from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    Numeric,
)
from sqlalchemy.schema import CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.infrastructure.database.base import Base, BasicString, DescriptionString, BoolFalse, BoolTrue, BasicNullString, IndexedUniqueString


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
    profile = relationship('Profile', back_populates='user',
                           uselist=False,
                           cascade='all, delete-orphan')
    authored_events = relationship('Event', back_populates='author')
    organizer_profile = relationship('Organizer',
                                     back_populates='user',
                                     cascade='all, delete-orphan')


class Organizer(Base):
    __tablename__ = 'organizers'
    # Foreign Keys.
    user_id = Column(Integer, ForeignKey('users.id', use_alter=True), unique=True)
    # Relationships.
    events = relationship('Event', back_populates='organizer')
    user = relationship('User', back_populates='organizer_profile')
    # Boolean fields.
    verified: Mapped[BoolFalse]
    # String fields.
    website: Mapped[BasicNullString]
    contact: Mapped[BasicNullString]
    name: Mapped[BasicString]
    description: Mapped[DescriptionString]
    logo_url: Mapped[BasicString] = mapped_column(unique=True)
    # Numeric fields
    number_of_events: Mapped[int] = mapped_column(Integer, default=0)
    rating: Mapped[float] = mapped_column(
        Numeric(3, 2),
        CheckConstraint('rating >= 0 AND rating <= 5'),
        default=0
    )



class Profile(Base):
    __tablename__ = 'profiles'
    # Foreign Keys.
    user_id = Column(
        Integer, ForeignKey('users.id', use_alter=True),
        unique=True, nullable=False
    )
    # Relationships.
    registered_events = relationship(
        'Event',
        back_populates='registered_participants',
        secondary='event_registrations'
    )
    user = relationship("User", back_populates="profile")
    # Boolean fields.
    notifications_enabled = Column(Boolean, default=True)
    # String fields.
    first_name: Mapped[BasicString]
    last_name: Mapped[BasicString]
    avatar_url: Mapped[BasicNullString]
    interested_technologies: Mapped[BasicNullString]
    location:  Mapped[BasicNullString]
