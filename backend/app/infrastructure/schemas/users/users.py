from datetime import datetime
from typing import Optional

from pydantic import EmailStr
from pydantic import field_validator, ValidationInfo

from backend.app.infrastructure.schemas.base import BaseModel
from backend.app.infrastructure.schemas.types import BasicString, PasswordString


class UserBase(BaseModel):
    username: BasicString
    email: EmailStr


class UserRead(UserBase):
    id: int
    created_at: datetime
    is_verified: bool
    is_active: bool


class UserCreate(UserBase):
    password: PasswordString
    password_confirm: PasswordString

    @field_validator('password_confirm')
    def passwords_match(cls, value: str, info: ValidationInfo) -> str:
        data = info.data
        if 'password' in data and value != data['password']:
            raise ValueError('Passwords do not match.')
        return value



class UserUpdate(UserBase):
    username: Optional[BasicString] = None
    email: Optional[BasicString] = None
    password: Optional[PasswordString] = None
    password_confirm: Optional[PasswordString] = None