from datetime import datetime


from ..types import BasicString, DescriptionField
from ..base import BaseModel


class CategoryBase(BaseModel):
    name: BasicString
    slug: str
    description: DescriptionField


class CategoryRead(CategoryBase):
    id: int
    created_at: datetime


class CategoryUpdate(CategoryBase):
    pass


class CategoryCreate(CategoryBase):
    pass
