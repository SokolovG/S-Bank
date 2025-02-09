from datetime import datetime


from backend.app.infrastructure.schemas.types import BasicString, DescriptionField
from backend.app.infrastructure.schemas.base import BaseModel


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
