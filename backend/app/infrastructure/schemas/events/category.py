from typing import Optional
from datetime import datetime

from pydantic import field_validator, model_validator

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
    @field_validator('slug')
    def validate_slug(cls, value: str) -> str:
        value = value.lower()
        return value

    @model_validator(mode='after')
    def validate_name_and_slug_different(self) -> "CategoryCreate":
        if self.name.lower() == self.slug:
            raise ValueError('Slug should not be identical to the name.')
        return self


class CategoryUpdate(CategoryBase):
    name: Optional[BasicString]
    slug: Optional[BasicString]
    description: Optional[DescriptionField]