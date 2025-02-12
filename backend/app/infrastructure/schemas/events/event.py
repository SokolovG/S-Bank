from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import HttpUrl

from backend.app.infrastructure.schemas.types import BasicString, DescriptionField
from backend.app.infrastructure.schemas.base import BaseModel


class EventBase(BaseModel):
    name: BasicString
    description: DescriptionField
    event_start_date: datetime
    event_end_date: datetime
    registration_deadline: datetime
    format: BasicString
    status: BasicString
    meeting_link: Optional[HttpUrl] = None
    timezone: BasicString
    max_participants: Optional[int] = None
    price: Optional[Decimal] = None
    currency: Optional[BasicString] = None
    current_participants: Optional[int] = 0


class EventRead(EventBase):
    id: int
    location_id: Optional[int]
    category_id: Optional[int]
    organizer_id: Optional[int]
    # Boolean fields.
    is_published: bool
    is_online: bool
    is_verify: bool
    # Date fields.
    pub_date: datetime

class EventCreate(EventBase):
    pass


class EventUpdate(EventBase):
    name: Optional[BasicString]
    description: Optional[DescriptionField]
    # Foreign Keys.
    organizer_id: Optional[int]
    location_id: Optional[int]
    category_id: Optional[int]
    # Enum fields
    format: Optional[BasicString] = None
    status: Optional[BasicString] = None
    currency: Optional[BasicString] = None
    # Boolean fields.
    is_published: Optional[bool] = None
    is_online: Optional[bool] = None
    is_verify: Optional[bool] = None
    # Date fields.
    pub_date: Optional[datetime] = None
    event_start_date: Optional[datetime] = None
    event_end_date: Optional[datetime] = None
    registration_deadline: Optional[datetime] = None
    # String fields.
    meeting_link: Optional[HttpUrl] = None
    timezone: Optional[BasicString] = None
    # Numeric fields
    max_participants: Optional[int] = None
    price: Optional[Decimal] = None
    current_participants: Optional[int] = None

