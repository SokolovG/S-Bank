from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import HttpUrl, ValidationInfo, field_validator

from backend.src.infrastructure.database.models.enums import (
    Currency,
    EventFormat,
    EventStatus,
)
from backend.src.interfaces.api.schemas.base import BaseModel
from backend.src.interfaces.api.schemas.types import DescriptionField, BasicString


class EventBase(BaseModel):
    """Base Pydantic schema for Event model.

    This class serves as a foundation for all Event-related schemas.
    All derived schemas inherit these base fields.

    Used as a parent class for:
    - EventRead: For retrieving events data
    - EventCreate: For creating new event
    - EventUpdate: For updating existing events
    """

    # Basic event information
    name: BasicString
    description: DescriptionField

    # Date and time fields
    event_start_date: datetime
    event_end_date: datetime
    registration_deadline: datetime
    timezone: BasicString

    # Event configuration
    format: EventFormat
    status: EventStatus
    meeting_link: Optional[HttpUrl] = None

    # Participation details
    max_participants: Optional[int] = None
    current_participants: Optional[int] = 0

    # Financial information
    price: Optional[Decimal] = None
    currency: Currency = Currency.USD

    @field_validator('event_end_date')
    def validate_end_date(cls, end_date: datetime, info: ValidationInfo) -> datetime:
        """Validate that event end date is after start date.

        Args:
            end_date: The event's end date
            info: Validation context containing all fields

        Returns:
            datetime: Validated end date

        Raises:
            ValueError: If end date is not after start date
        """
        data = info.data
        start_date = data.get('event_start_date')
        if start_date and end_date <= start_date:
            raise ValueError('End date must be after start date.')
        return end_date

    @field_validator('registration_deadline')
    def deadline_before_start(cls, deadline: datetime, info: ValidationInfo) -> datetime:
        """Validate that registration deadline is before event start.

        Args:
            deadline: The registration deadline
            info: Validation context containing all fields

        Returns:
            datetime: Validated deadline

        Raises:
            ValueError: If deadline is not before event start
        """
        data = info.data
        start_date = data.get('event_start_date')
        if start_date and deadline >= start_date:
            raise ValueError('Registration deadline must be before event start.')
        return deadline

    @field_validator('current_participants')
    def validate_number_of_participants(cls, current: int, info: ValidationInfo) -> int:
        """Validate that current participants don't exceed maximum.

        Args:
            current: Number of current participants
            info: Validation context containing all fields

        Returns:
            int: Validated number of participants

        Raises:
            ValueError: If current participants exceed maximum
        """
        data = info.data
        max_number = data.get('max_participants')
        if max_number and current > max_number:
            raise ValueError('Current participants cannot exceed maximum.')
        return current

    @field_validator('price')
    def validate_price_currency(cls, price: Optional[Decimal], info: ValidationInfo) -> Optional[Decimal]:
        """Validate price and currency relationship.

        Args:
            price: Event price
            info: Validation context containing all fields

        Returns:
            Optional[Decimal]: Validated price or None

        Raises:
            ValueError: If currency is missing when price is set
        """
        if price is None:
            return None

        currency = info.data.get('currency', Currency.USD)

        if not currency:
            raise ValueError('Currency must be specified when price is set')

        return price

class EventRead(EventBase):
    """Schema for reading event data.

    Extends EventBase with additional fields needed for data retrieval.
    """

    # Identification fields
    id: int
    location_id: Optional[int]
    category_id: int
    organizer_id: int

    # Status flags
    is_published: bool
    is_online: bool
    is_verify: bool

    # Publication information
    pub_date: datetime


class EventCreate(EventBase):
    """Schema for creating new events.

    Extends EventBase with fields required for event creation.
    """

    # Relationship fields
    location_id: Optional[int] = None
    category_id: Optional[int] = None
    organizer_id: Optional[int] = None


class EventUpdate(EventBase):
    """Schema for updating existing event.

    Notes:
        - All fields are optional to allow partial updates
        - Only changed fields need to be included in request
        - Validation from base class still applies to provided fields
    """

    # Basic information
    name: Optional[BasicString] = None
    description: Optional[DescriptionField] = None

    # Relationships
    organizer_id: Optional[int] = None
    location_id: Optional[int] = None
    category_id: Optional[int] = None

    # Classification
    format: Optional[EventFormat] = EventFormat.OFFLINE
    status: Optional[EventStatus] = EventStatus.PLANNED
    currency: Optional[Currency] = Currency.USD

    # Status flags
    is_published: Optional[bool] = None
    is_online: Optional[bool] = None
    is_verify: Optional[bool] = None

    # Dates
    pub_date: Optional[datetime] = None
    event_start_date: Optional[datetime] = None
    event_end_date: Optional[datetime] = None
    registration_deadline: Optional[datetime] = None

    # Additional details
    meeting_link: Optional[HttpUrl] = None
    timezone: Optional[BasicString] = None
    max_participants: Optional[int] = None
    price: Optional[Decimal] = None
    current_participants: Optional[int] = None
