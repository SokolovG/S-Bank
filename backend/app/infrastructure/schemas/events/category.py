from typing import Optional
from datetime import datetime

from backend.app.infrastructure.schemas.base import BaseModel
from backend.app.infrastructure.schemas.types import BasicString, DescriptionField


class CategoryBase(BaseModel):
    name: BasicString
    slug: BasicString
    description: DescriptionField


class CategoryRead(CategoryBase):
    id: int
    created_at: datetime


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    name: Optional[BasicString]
    slug: Optional[BasicString]
    description: Optional[DescriptionField]