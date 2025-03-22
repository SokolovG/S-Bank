from datetime import datetime
from decimal import Decimal

from pydantic import AnyUrl, Field, HttpUrl

from backend.src.interfaces.api.schemas.base_dto import BasePydanticModel
from backend.src.interfaces.api.schemas.custom_types import BasicString, DescriptionField


class OrganizerBase(BasePydanticModel):
    """Base Pydantic schema for the Organizer model.

    This class serves as a foundation for all organizer-related schemas.
    All derived schemas inherit these base fields:
    Used as a parent class for:
    - OrganizerRead: For retrieving organizer data
    - OrganizerCreate: For creating new organizer
    - OrganizerUpdate: For updating existing organizer_model.py
    """

    website: HttpUrl | None = None
    contact: BasicString | None = None
    name: BasicString
    description: DescriptionField
    logo_url: AnyUrl | None = None


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

    website: HttpUrl | None = None
    contact: BasicString | None = None
    name: BasicString | None = None
    description: DescriptionField | None = None
    logo_url: AnyUrl | None = None
