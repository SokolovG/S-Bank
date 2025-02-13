from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import HttpUrl, field_validator, ValidationInfo

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
    currency: BasicString
    current_participants: Optional[int] = 0

    @field_validator('event_end_date')
    def event_start_date(cls, end_date: datetime, info: ValidationInfo) -> datetime:
        data = info.data
        start_date = data.get('event_start_date')
        if start_date and end_date <= start_date:
            raise ValueError('End date must be after start date.')
        return end_date

    @field_validator('registration_deadline')
    def deadline_before_start(cls, deadline: datetime, info: ValidationInfo) -> datetime:
        data = info.data
        start_date = data.get('event_start_date')
        if start_date and deadline >= start_date:
            raise ValueError('Registration deadline must be before event start.')
        return deadline

    @field_validator('current_participants')
    def validate_number_of_participants(cls, current: int, info: ValidationInfo) -> int:
        data = info.data
        max_number = data.get('max_participants')
        if max_number and current > max_number:
            raise ValueError('Current participants cannot exceed maximum.')
        return current

    @field_validator('price')
    def validate_price_currency(cls, price: Decimal, info: ValidationInfo) -> Decimal:
        data = info.data
        if price and price > 0 and 'currency' not in data:
            raise ValueError('Currency must be specified when price is set.')
        elif not data['currency']:
            raise ValueError('Currency cannot be empty when price is set.')

        return price

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
    location_id: Optional[int]
    category_id: Optional[int]
    organizer_id: Optional[int]


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