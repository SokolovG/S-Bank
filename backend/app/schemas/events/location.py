from datetime import datetime

from ..types import BasicString
from ..base import BaseModel


class LocationBase(BaseModel):
    name: BasicString
    address: BasicString
    city: BasicString
    country: BasicString


class LocationRead(LocationBase):
    id: int
    created_at: datetime


class LocationUpdate(LocationBase):
    pass


class LocationCreate(BaseModel):
    pass
