"""Basic custom types module for Pydantic schemas.

This module defines reusable field types with validation rules for use across
the application's Pydantic models. Each type is defined with specific length
constraints and validation rules.

Available types:
- BasicString: For standard text fields
- DescriptionField: For longer text content
- PasswordString: For password fields with length validation
"""

from typing import Annotated
from pydantic import Field

from backend.app.constants import (
    MAX_BASIC_LENGTH,
    MAX_DESCRIPTION_LENGTH,
    MIN_BASIC_LENGTH,
    PASSWORD_MIN_LENGTH
)


BasicString = Annotated[
    str,
    Field(
        min_length=MIN_BASIC_LENGTH,
        max_length=MAX_BASIC_LENGTH,
        description='Standard text field with length validation',

    )
]

DescriptionField = Annotated[
    str,
    Field(
        min_length=MIN_BASIC_LENGTH,
        max_length=MAX_DESCRIPTION_LENGTH,
        description='Extended text field for detailed content',
    )
]

PasswordString = Annotated[
    str,
    Field(
        min_length=PASSWORD_MIN_LENGTH,
        max_length=MAX_BASIC_LENGTH,
        description='Password field with length validation',
    )
]