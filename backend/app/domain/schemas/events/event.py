from datetime import datetime
from typing import Optional
from pydantic import condecimal, Field

from backend.app.domain.schemas.types import BasicString, DescriptionField
from backend.app.domain.schemas.events.category import CategoryRead, CategoryUpdate
from backend.app.domain.models import EventFormat, EventStatus, Currency
from backend.app.domain.schemas.events.location import LocationRead, LocationUpdate
from backend.app.domain.schemas.users.organizer import OrganizerRead
from backend.app.domain.schemas.base import BaseModel


class EventBase(BaseModel):
    name: BasicString
    description: DescriptionField


class EventRead(EventBase):
    id: int
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
    format: EventFormat
    status: EventStatus
    meeting_link: Optional[BasicString] = None
    timezone: str
    # Integer fields
    max_participants: Optional[int] = None
    price: Optional[condecimal(max_digits=10, decimal_places=2)]
    currency: Optional[Currency] = None
    current_participants: Optional[int]


class EventCreate(EventBase):
    location: Optional[LocationRead] = None
    category_id: int
    organizer_id: int

    # Boolean fields
    is_online: bool = False
    is_published: bool = False
    is_verify: bool = False

    # Enum fields
    format: EventFormat = EventFormat.OFFLINE
    status: EventStatus = EventStatus.PLANNED

    # Date fields
    event_start_date: datetime
    event_end_date: datetime
    registration_deadline: datetime

    # String fields
    meeting_link: Optional[BasicString] = None
    timezone: str = 'UTC'

    # Number fields
    max_participants: Optional[int] = Field(default=None, ge=0)
    price: Optional[condecimal(max_digits=10, decimal_places=2)] = Field(default=None, ge=0)
    currency: Optional[Currency] = None
    current_participants: Optional[int] = Field(default=0, ge=0)


class EventUpdate(EventBase):
    name: BasicString
    description: DescriptionField
    location: Optional[LocationUpdate] = None
    category: CategoryUpdate
    is_online: bool
    event_start_date: Optional[datetime]
    event_end_date: Optional[datetime]
    registration_deadline: Optional[datetime]
    format: Optional[EventFormat] = None
    status: Optional[EventStatus] = None
    meeting_link: Optional[BasicString] = None
    timezone: Optional[str]
    max_participants: Optional[int] = None
    price: Optional[condecimal(max_digits=10, decimal_places=2)]
    currency: Optional[Currency] = None
    current_participants: Optional[int]
