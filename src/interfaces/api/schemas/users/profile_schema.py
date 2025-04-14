from datetime import date, datetime

from pydantic import AnyUrl, field_validator

from src.interfaces.api.schemas.base_dto import BasePydanticModel
from src.interfaces.api.schemas.custom_types import BasicString


class ProfileBase(BasePydanticModel):
    """Base Pydantic schema for Profile model.

    This class serves as a foundation for all User-related schemas.
    All derived schemas inherit these base fields:
    Used as a parent class for:
    - ProfileRead: For retrieving profile data
    - ProfileCreate: For creating new profiles
    - ProfileUpdate: For updating existing profiles

    Extends UserBase with additional validation:
    - Passwords match validation

    Validation rules:
    1. The date of birth cannot be in the future.
    """

    notifications_enabled: bool
    interested_technologies: BasicString | None = None
    location: BasicString | None = None
    first_name: BasicString
    last_name: BasicString
    avatar_url: AnyUrl | None = None
    birth_date: date
    gender: BasicString | None

    @field_validator('birth_date')
    def validate_birth_date(cls, value: date) -> date:
        """Validate that password and password_confirm match.

        Args:
            value: birth_date
        Returns:
            birth_date if validated

        """
        if value > date.today():
            raise ValueError('Birth date cannot be in the future.')
        return value


class ProfileRead(ProfileBase):
    """Schema for reading Profile data."""

    user_id: int
    id: int
    created_at: datetime


class ProfileCreate(ProfileBase):
    """Schema for creating new profile."""


class ProfileUpdate(ProfileBase):
    """Schema for updating existing profile.

    Notes:
    - All fields are optional to allow partial updates
    - Only changed fields need to be included in request
    - Validation from base class still applies to provided fields

    """

    notifications_enabled: bool | None = None
    interested_technologies: BasicString | None = None
    location: BasicString | None = None
    first_name: BasicString | None = None
    last_name: BasicString | None = None
    avatar_url: AnyUrl | None = None
    birth_date: date | None = None
    gender: BasicString | None = None
