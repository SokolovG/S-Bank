from pydantic import BaseModel, Field

from ..types import BasicString, DescriptionField

class LocationRead(BaseModel):
    id: int
    name: BasicString
    address: BasicString
    city: BasicString
    country: BasicString