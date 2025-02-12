from enum import Enum


class EventFormat(str, Enum):
    ONLINE = 'online'
    OFFLINE = 'offline'
    HYBRID = 'hybrid'


class EventStatus(str, Enum):
    PLANNED = 'planned'
    ONGOING = 'ongoing'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'


class Currency(str, Enum):
    USD = 'USD'
    EUR = 'EUR'
    RUB = ' RUB'


class ParticipantStatus(str, Enum):
    REGISTERED = 'registered'
    CONFIRMED = 'confirmed'
    WAITLISTED = 'waitlisted'
    CANCELLED = 'cancelled'
    ATTENDED = 'attended'
    NO_SHOW = 'no_show'