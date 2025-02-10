from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum as SQLAlchemyEnum,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Table,
)
from sqlalchemy.orm import relationship

from backend.app.constants import MAX_BASIC_LENGTH, MAX_DESCRIPTION_LENGTH
from backend.app.infrastructure.database.base import Base
from backend.app.infrastructure.models.enums import Currency, EventFormat, EventStatus



class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # String fields.
    name = Column(String(MAX_BASIC_LENGTH), nullable=False)
    address = Column(String(MAX_BASIC_LENGTH))
    city = Column(String(MAX_BASIC_LENGTH), index=True)
    country = Column(String(MAX_BASIC_LENGTH), index=True)
    # Date fields.
    created_at = Column(DateTime, default=datetime.utcnow)
    # Relationships.
    events = relationship('Event', back_populates='location')


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # String fields.
    name = Column(String(MAX_BASIC_LENGTH), nullable=False)
    slug = Column(
        String(MAX_BASIC_LENGTH),
        unique=True, nullable=False, index=True
    )
    description = Column(String(MAX_DESCRIPTION_LENGTH), nullable=True)
    # Date fields.
    created_at = Column(DateTime, default=datetime.utcnow)
    # Relationships.
    events = relationship('Event', back_populates='category')


event_registrations = Table(
    'event_registrations',
    Base.metadata,
    Column('profile_id', Integer, ForeignKey('profiles.id', use_alter=True)),
    Column('event_id', Integer, ForeignKey('events.id', use_alter=True)),
)


class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(MAX_BASIC_LENGTH), nullable=False, index=True)
    description = Column(
        String(MAX_DESCRIPTION_LENGTH),
        nullable=False
    )
    # Foreign Keys.
    author_id = Column(Integer, ForeignKey('users.id', use_alter=True))
    location_id = Column(
        Integer,
        ForeignKey('locations.id', use_alter=True),
        nullable=True
    )
    organizer_id = Column(
        Integer,
        ForeignKey('organizers.id', use_alter=True),
    )
    category_id = Column(
        Integer, ForeignKey('categories.id', use_alter=True),
    )
    # Relationships.
    author = relationship('User', back_populates='authored_events')
    organizer = relationship('Organizer', back_populates='events')
    location = relationship('Location', back_populates='events')
    category = relationship('Category', back_populates='events')
    registered_participants = relationship(
        "Profile",
        secondary=event_registrations,
        back_populates="registered_events"
    )
    # Enum fields
    format = Column(
        SQLAlchemyEnum(EventFormat),
        default=EventFormat.OFFLINE,
        nullable=False
    )
    status = Column(
        SQLAlchemyEnum(EventStatus),
        default=EventStatus.PLANNED, nullable=False
    )
    currency = Column(SQLAlchemyEnum(Currency), default=Currency.USD)
    # Boolean fields.
    is_published = Column(Boolean, default=False)
    is_online = Column(Boolean, default=False)
    is_verify = Column(Boolean, default=False)
    # Date fields.
    pub_date = Column(DateTime)
    event_start_date = Column(DateTime)
    event_end_date = Column(DateTime)
    registration_deadline = Column(DateTime, nullable=True)
    # String fields.
    meeting_link = Column(String(MAX_BASIC_LENGTH), nullable=True)
    timezone = Column(String(MAX_BASIC_LENGTH), default='UTC')
    # Numeric fields
    max_participants = Column(Integer, nullable=True)
    price = Column(Numeric(10, 2), nullable=True)
    current_participants = Column(Integer, nullable=True)


