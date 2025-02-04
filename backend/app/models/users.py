from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Numeric, ForeignKey
from sqlalchemy.schema import CheckConstraint

from .database.connection import Base
from .constants import MAX_BASIC_LENGTH, MAX_TEXT_LENGTH


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # String fields.
    username = Column(String(MAX_BASIC_LENGTH), unique=True, index=True)
    email = Column(String(MAX_BASIC_LENGTH), unique=True, index=True)

    # Relationships.
    profile = relationship('Profile', back_populates='user')
    authored_events = relationship('Event', back_populates='author', uselist=False)
    organizer_profile = relationship('Organizer', back_populates='user')


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
    description = Column(Text(MAX_TEXT_LENGTH), nullable=False)
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
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    # Relationships.
    registered_events = relationship('Event', back_populates='registered_participants', secondary='event_registrations')
    user = relationship("User", back_populates="profile")
    # Boolean fields.
    notifications_enabled = Column(Boolean, default=True)
    # Date fields.
    created_at = Column(DateTime, default=datetime.utcnow)
    # String fields.
    interested_technologies = Column(String(MAX_BASIC_LENGTH), nullable=True)
    location = Column(String(30), nullable=True)


