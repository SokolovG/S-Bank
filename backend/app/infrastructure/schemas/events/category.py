from datetime import datetime
from typing import Optional, Self

from pydantic import field_validator, model_validator

from backend.app.infrastructure.schemas.base import BaseModel
from backend.app.infrastructure.schemas.types import BasicString, DescriptionField


class CategoryBase(BaseModel):
    """Base Pydantic schema for Category model.

    This class serves as a foundation for all Category-related schemas.
    All derived schemas inherit these base fields:
    Used as a parent class for:
    - CategoryRead: For retrieving category data
    - CategoryCreate: For creating new categories
    - CategoryUpdate: For updating existing categories
    """

    name: BasicString
    slug: BasicString
    description: DescriptionField


class CategoryRead(CategoryBase):
    """Schema for reading category data."""

    id: int
    created_at: datetime


class CategoryCreate(CategoryBase):
    """Schema for creating new categories with validation.

    Extends CategoryBase with additional validation:
    - Enforces lowercase slugs
    - Ensures slug differs from name

    Validation rules:
    1. Slug is automatically converted to lowercase
    2. Slug cannot be identical to name (case-insensitive)
    """

    @field_validator("slug")
    def validate_slug(cls, value: str) -> str:
        """Validate and transform slug to lowercase.

        Args:
            value: Original slug string
        Returns:
            Lowercase slug string
        """
        value = value.lower()
        return value

    @model_validator(mode="after")
    def validate_name_and_slug_different(self) -> Self:
        """Validate that name and slug are not identical.

        Returns:
            Self instance if validation passes
        Raises:
            ValueError: If slug matches name (case-insensitive)
        """
        if self.name.lower() == self.slug:
            raise ValueError("Slug should not be identical to the name.")
        return self


class CategoryUpdate(CategoryBase):
    """Schema for updating existing categories.

    Extends CategoryBase by making all fields optional:
    - name: Optional new category name
    - slug: Optional new URL-friendly identifier
    - description: Optional new description

    Notes:
    - All fields are optional to allow partial updates
    - Only changed fields need to be included in request
    - Validation from base class still applies to provided fields
    """

    name: Optional[BasicString] = None
    slug: Optional[BasicString] = None
    description: Optional[DescriptionField] = None
