from pydantic import BaseModel

from ..types import BasicString,  DescriptionField


class CategoryRead(BaseModel):
    id: int
    name: BasicString
    slug: str
    description: DescriptionField
    country: BasicString