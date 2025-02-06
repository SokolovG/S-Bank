from datetime import datetime
from typing import Optional

from pydantic import BaseModel, condecimal, Field

from ..types import BasicString, DescriptionField


class OrganizerBase(BaseModel):
    user_id: str
    website: BasicString
    contact: BasicString
    name: BasicString
    description: DescriptionField


class OrganizerRead(OrganizerBase):
    id: int
    verified: bool
    created_at: datetime
    number_of_events: int
    rating: Optional[condecimal(max_digits=3, decimal_places=2)] = Field(None, ge=0, le=5)


class OrganizerCreate(OrganizerBase):
    pass


class OrganizerUpdate(BaseModel):
    user_id: Optional[str] = None
    website: Optional[BasicString] = None
    contact: Optional[BasicString] = None
    name: Optional[BasicString] = None
    description: Optional[DescriptionField] = None