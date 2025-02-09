from datetime import datetime
from typing import Optional

from pydantic import condecimal, Field

from backend.app.infrastructure.schemas.types import BasicString, DescriptionField
from backend.app.infrastructure.schemas.base import BaseModel


class OrganizerBase(BaseModel):
    user_id: int
    website: Optional[BasicString]
    contact: Optional[BasicString]
    name: BasicString
    description: DescriptionField
    logo_url: BasicString


class OrganizerRead(OrganizerBase):
    id: int
    verified: bool
    created_at: datetime
    number_of_events: int
    rating: Optional[condecimal(max_digits=3, decimal_places=2)] = Field(
        None,
        ge=0,
        le=5
    )


class OrganizerCreate(OrganizerBase):
    pass


class OrganizerUpdate(BaseModel):
    user_id: Optional[str] = None
    website: Optional[BasicString] = None
    contact: Optional[BasicString] = None
    name: Optional[BasicString] = None
    description: Optional[DescriptionField] = None
    logo_url: Optional[BasicString]
