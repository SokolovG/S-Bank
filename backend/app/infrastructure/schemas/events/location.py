from datetime import datetime
from typing import Optional

from backend.app.infrastructure.schemas.types import BasicString
from backend.app.infrastructure.schemas.base import BaseModel


class LocationBase(BaseModel):
    name: BasicString
    address: BasicString
    city: BasicString
    country: BasicString


class LocationRead(LocationBase):
    id: int
    created_at: datetime


class LocationCreate(BaseModel):
    pass


class LocationUpdate(LocationBase):
    name: Optional[BasicString]
    address: Optional[BasicString]
    city: Optional[BasicString]
    country: Optional[BasicString]
