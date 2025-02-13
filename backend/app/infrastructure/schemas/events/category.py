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
    @classmethod
    def validate_slug(cls, v):
        v = v.lower()
        return v

    @model_validator(mode='after')
    @classmethod
    def validate_name_and_slug_different(cls, data):
        if data.name.lower() == data.slug:
            raise ValueError('Slug should not be identical to the name.')
        return data


class CategoryUpdate(CategoryBase):
    name: Optional[BasicString]
    slug: Optional[BasicString]
    description: Optional[DescriptionField]