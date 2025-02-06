from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from ..types import BasicString


class ProfileBase(BaseModel):
    user_id: int
    notifications_enabled: bool
    interested_technologies: Optional[BasicString]
    location: Optional[BasicString]


class ProfileRead(ProfileBase):
    id: int
    created_at: datetime


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(BaseModel):
    notifications_enabled: Optional[bool] = True
    interested_technologies: Optional[BasicString] = None
    location: Optional[BasicString] = None

