from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import Field, HttpUrl, AnyUrl

from backend.app.infrastructure.schemas.types import BasicString, DescriptionField
from backend.app.infrastructure.schemas.base import BaseModel


class OrganizerBase(BaseModel):
    website: Optional[HttpUrl] = None
    contact: Optional[BasicString] = None
    name: BasicString
    description: DescriptionField
    logo_url: Optional[AnyUrl] = None


class OrganizerRead(OrganizerBase):
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
    pass


class OrganizerUpdate(OrganizerBase):
    website: Optional[HttpUrl] = None
    contact: Optional[BasicString] = None
    name: Optional[BasicString] = None
    description: Optional[DescriptionField] = None
    logo_url: Optional[AnyUrl] = None