from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import Field, HttpUrl, AnyUrl

from backend.app.infrastructure.schemas.types import BasicString, DescriptionField
from backend.app.infrastructure.schemas.base import BaseModel


class OrganizerBase(BaseModel):
    """Base Pydantic schema for Organizer model.

    This class serves as a foundation for all organizer-related schemas.
    All derived schemas inherit these base fields:
    Used as a parent class for:
    - OrganizerRead: For retrieving organizer data
    - OrganizerCreate: For creating new organizer
    - OrganizerUpdate: For updating existing organizers
    """
    website: Optional[HttpUrl] = None
    contact: Optional[BasicString] = None
    name: BasicString
    description: DescriptionField
    logo_url: Optional[AnyUrl] = None


class OrganizerRead(OrganizerBase):
    """Schema for reading organizer data."""
    id: int
    user_id: int
    verified: bool
    created_at: datetime
    rating: Decimal = Field(
        default=0,
        ge=0,
        le=5,
        decimal_places=2,
        description="Organizer rating from 0 to 5"
    )


class OrganizerCreate(OrganizerBase):
    """Schema for creating new organizer."""


class OrganizerUpdate(OrganizerBase):
    """Schema for updating existing organizer.

    Notes:
    - All fields are optional to allow partial updates
    - Only changed fields need to be included in request
    - Validation from base class still applies to provided fields
    """
    website: Optional[HttpUrl] = None
    contact: Optional[BasicString] = None
    name: Optional[BasicString] = None
    description: Optional[DescriptionField] = None
    logo_url: Optional[AnyUrl] = None