from datetime import datetime

from sqlalchemy import (
   Boolean,
   Column,
   DateTime,
   ForeignKey,
   Integer,
   Numeric,
   String,
)
from sqlalchemy.schema import CheckConstraint
from sqlalchemy.orm import relationship

from backend.app.constants import MAX_BASIC_LENGTH, MAX_DESCRIPTION_LENGTH
from backend.app.database.connection import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # String fields.
    username = Column(String(MAX_BASIC_LENGTH), unique=True, index=True)
    email = Column(String(MAX_BASIC_LENGTH), unique=True, index=True)
    hashed_password = Column(String(MAX_BASIC_LENGTH))
    # Datetime fields
    created_at = Column(DateTime, default=datetime.utcnow)
    # Boolean fields
    is_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
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
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Foreign Keys.
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    # Relationships.
    events = relationship('Event', back_populates='organizer')
    user = relationship('User', back_populates='organizer_profile')
    # Boolean fields.
    verified = Column(Boolean, default=False)
    # Date fields.
    created_at = Column(DateTime, default=datetime.utcnow)
    # String fields.
    website = Column(String(MAX_BASIC_LENGTH), nullable=True)
    contact = Column(String(MAX_BASIC_LENGTH), nullable=True)
    name = Column(String(MAX_BASIC_LENGTH), nullable=False)
    description = Column(String(MAX_DESCRIPTION_LENGTH), nullable=False)
    logo_url = Column(String(MAX_BASIC_LENGTH), unique=True)
    # Numeric fields
    number_of_events = Column(Integer, default=0)
    rating = Column(
        Numeric(3, 2),
        CheckConstraint('rating >= 0 AND rating <= 5'),
        default=0)


class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Foreign Keys.
    user_id = Column(
        Integer, ForeignKey('users.id'),
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
    # Date fields.
    created_at = Column(DateTime, default=datetime.utcnow)
    # String fields.
    first_name = Column(String(MAX_BASIC_LENGTH))
    last_name = Column(String(MAX_BASIC_LENGTH))
    avatar_url = Column(String(MAX_BASIC_LENGTH), nullable=True)
    interested_technologies = Column(String(MAX_BASIC_LENGTH), nullable=True)
    location = Column(String(MAX_BASIC_LENGTH), nullable=True)
