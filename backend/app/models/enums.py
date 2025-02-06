from enum import Enum


class EventFormat(str, Enum):
    ONLINE = 'online'
    OFFLINE = 'offline'
    Hybrid = 'hybrid'


class EventStatus(str, Enum):
    PLANNED = 'planned'
    ONGOING = 'ongoing'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'


class Currency(str, Enum):
    USD = 'USD'
    EUR = 'EUR'
    RUB = ' RUB'
