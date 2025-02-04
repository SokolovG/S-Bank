from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Numeric, Table
from sqlalchemy.orm import relationship
from sqlalchemy import Enum as SQLAlchemyEnum
from datetime import datetime

from backend.app.database.connection import Base
from .constants import MAX_BASIC_LENGTH, MAX_TEXT_LENGTH
from .enums import Currency, EventFormat, EventStatus


event_registrations = Table(
    'event_registrations',
    Base.metadata,
    Column('profile_id', Integer, ForeignKey('profiles.id')),
    Column('event_id', Integer, ForeignKey('events.id')),
)


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
    slug = Column(String(MAX_BASIC_LENGTH), unique=True, nullable=False, index=True)
    description = Column(Text(MAX_TEXT_LENGTH), nullable=True)
    # Date fields.
    created_at = Column(DateTime, default=datetime.utcnow)
    # Relationships.
    events = relationship('Event', back_populates='category')


class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(MAX_BASIC_LENGTH), nullable=False, index=True)
    description = Column(String(MAX_BASIC_LENGTH), nullable=False)
    # Foreign Keys.
    author_id = Column(Integer, ForeignKey('users.id'), ondelete='SET NULL', nullable=True)
    location_id = Column(Integer, ForeignKey('locations.id'), ondelete='SET NULL', nullable=True)
    organizer_id = Column(Integer, ForeignKey('organizers.id'), ondelete='CASCADE')
    category_id = Column(Integer, ForeignKey('categories.id'), ondelete='SET NULL', nullable=True)
    # Relationships.
    author = relationship('User', back_populates='events')
    organizer = relationship('Organizer', back_populates='events')
    location = relationship('Location', back_populates='events')
    category = relationship('Category', back_populates='events')
    registered_participants = relationship(
        "Profile",
        secondary=event_registrations,
        back_populates="registered_events"
    )
    # Enum fields
    format = Column(SQLAlchemyEnum(EventStatus), default=EventFormat.OFFLINE, nullable=False)
    status = Column(SQLAlchemyEnum(EventFormat), default=EventStatus.PLANNED, nullable=False)
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
    meeting_link = Column(String(MAX_BASIC_LENGTH))
    timezone = Column(String(MAX_BASIC_LENGTH), default='UTC')
    # Numeric fields
    max_participants = Column(Integer, nullable=True)
    price = Column(Numeric(10, 2), nullable=True)
    currency = Column(SQLAlchemyEnum(Currency), default=Currency.USD)
    current_participants = Column(Integer, nullable=True)