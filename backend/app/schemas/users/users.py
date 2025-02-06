from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from ..types import BasicString


class UserBase(BaseModel):
    username: BasicString
    email: BasicString
    hashed_password: BasicString


class UserRead(UserBase):
    id: int
    created_at: datetime
    is_verified: bool
    is_active: bool

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    username: Optional[BasicString]
    email: Optional[BasicString]