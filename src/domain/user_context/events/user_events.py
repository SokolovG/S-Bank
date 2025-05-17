from dataclasses import dataclass, field
from datetime import datetime

from src.domain.user_context.value_objects import UserId


@dataclass(frozen=True)
class UserRegisteredEvent:
    user_id: UserId
    email: str
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass(frozen=True)
class UserVerifiedEvent:
    user_id: UserId
    email: str
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass(frozen=True)
class UserBlockedEvent:
    user_id: UserId
    email: str
    reason: str
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass(frozen=True)
class UserUnlockedEvent:
    user_id: UserId
    email: str
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass(frozen=True)
class UserDeactivatedEvent:
    user_id: UserId
    email: str
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass(frozen=True)
class UserEmailChangedEvent:
    user_id: UserId
    old_email: str
    new_email: str
    timestamp: datetime = field(default_factory=datetime.now)
