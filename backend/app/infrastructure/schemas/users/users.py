from datetime import datetime
from typing import Optional

from pydantic import EmailStr
from pydantic import field_validator, ValidationInfo

from backend.app.infrastructure.schemas.base import BaseModel
from backend.app.infrastructure.schemas.types import BasicString, PasswordString


class UserBase(BaseModel):
    """Base Pydantic schema for User model.

    This class serves as a foundation for all User-related schemas.
    All derived schemas inherit these base fields:
    Used as a parent class for:
    - UserRead: For retrieving users data
    - UserCreate: For creating new users
    - UserUpdate: For updating existing users
    """

    username: BasicString
    email: EmailStr


class UserRead(UserBase):
    """Schema for reading user data."""

    id: int
    created_at: datetime
    is_verified: bool
    is_active: bool


class UserCreate(UserBase):
    """Schema for creating new user.

    Extends UserBase with additional validation:
    - Passwords match validation

    Validation rules:
    1. The password must coincide
    """

    password: PasswordString
    password_confirm: PasswordString

    @field_validator('password_confirm')
    def passwords_match(cls, value: str, info: ValidationInfo) -> str:
        """Validate that password and password_confirm match.

        Args:
            value: password_confirm
        Returns:
            password_confirm if validated
        """
        data = info.data
        if 'password' in data and value != data['password']:
            raise ValueError('Passwords do not match.')
        return value


class UserUpdate(UserBase):
    """Schema for updating existing user.

    Notes:
    - All fields are optional to allow partial updates
    - Only changed fields need to be included in request
    - Validation from base class still applies to provided fields
    """

    username: Optional[BasicString] = None
    email: Optional[BasicString] = None
    password: Optional[PasswordString] = None
    password_confirm: Optional[PasswordString] = None
