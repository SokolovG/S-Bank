from datetime import date, datetime
from typing import Optional

from pydantic import AnyUrl, field_validator

from backend.app.infrastructure.schemas.types import BasicString
from backend.app.infrastructure.schemas.base import BaseModel


class ProfileBase(BaseModel):
    notifications_enabled: bool
    interested_technologies: Optional[BasicString] = None
    location: Optional[BasicString] = None
    first_name: BasicString
    last_name: BasicString
    avatar_url: Optional[AnyUrl] = None
    birth_date: date
    gender: Optional[BasicString]

    @field_validator('birth_date')
    def validate_birth_date(cls, value: str) -> str:
        if value > date.today():
            raise ValueError('Birth date cannot be in the future.')
        return value
class ProfileRead(ProfileBase):
    user_id: int
    id: int
    created_at: datetime


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(ProfileBase):
    notifications_enabled: Optional[bool] = None
    interested_technologies: Optional[BasicString] = None
    location: Optional[BasicString] = None
    first_name: Optional[BasicString] = None
    last_name: Optional[BasicString] = None
    avatar_url: Optional[AnyUrl] = None
    birth_date: Optional[date] = None
    gender: Optional[BasicString] = None