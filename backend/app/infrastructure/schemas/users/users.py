from datetime import datetime
from typing import Optional

from pydantic import EmailStr

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


class UserUpdate(UserBase):
    username: Optional[BasicString] = None
    email: Optional[BasicString] = None
    password: Optional[PasswordString] = None
    password_confirm: Optional[PasswordString] = None