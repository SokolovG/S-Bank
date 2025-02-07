from datetime import datetime
from typing import Optional

from ..types import BasicString
from ..base import BaseModel


class ProfileBase(BaseModel):
    user_id: int
    notifications_enabled: bool
    interested_technologies: Optional[BasicString]
    location: Optional[BasicString]
    first_name: BasicString
    last_name: BasicString
    avatar_url: BasicString


class ProfileRead(ProfileBase):
    id: int
    created_at: datetime


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(BaseModel):
    notifications_enabled: Optional[bool] = True
    interested_technologies: Optional[BasicString] = None
    location: Optional[BasicString] = None
    first_name: Optional[BasicString] = None
    last_name: Optional[BasicString] = None
    avatar_url: Optional[BasicString] = None
