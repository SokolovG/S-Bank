from datetime import datetime
from typing import Optional
from pydantic import BaseModel, condecimal

from ..types import BasicString, DescriptionField
from .category import CategoryRead
from .location import LocationRead
from ..users.organizer import OrganizerRead

class BaseEvent(BaseModel):
    id: int
    name: BasicString
    description: DescriptionField


class EventRead(BaseEvent):
    id: int
    # Other schemas
    location: Optional[LocationRead] = None
    category: CategoryRead
    organizer: OrganizerRead
    # Boolean fields.
    is_published: bool
    is_online: bool
    is_verify: bool
    # Date fields.
    pub_date: datetime
    event_start_date: datetime
    event_end_date: datetime
    registration_deadline: datetime
    # String fields
    format: str
    status: str
    meeting_link: BasicString
    timezone: str
    # Integer fields
    max_participants: int
    price: Optional[condecimal(max_digits=10, decimal_places=2)]
    currency: str
    current_participants: int

class EventCreate(BaseEvent):
    pass


class EventUpdate(BaseModel):
    pass

