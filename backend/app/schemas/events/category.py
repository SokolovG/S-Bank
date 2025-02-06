from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from ..types import BasicString,  DescriptionField


class CategoryBase(BaseModel):
    name: BasicString
    slug: str
    description: Optional[DescriptionField]


class CategoryRead(CategoryBase):
    id: int
    created_at: datetime


class CategoryUpdate(CategoryBase):
    pass