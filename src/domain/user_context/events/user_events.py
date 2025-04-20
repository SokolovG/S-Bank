from dataclasses import dataclass, field
from datetime import datetime

from src.domain.user_context.value_objects import UserId


@dataclass(frozen=True)
class UserRegisteredEvent:
    user_id: UserId
    email: str
    timestamp: datetime = field(default_factory=datetime.now)
