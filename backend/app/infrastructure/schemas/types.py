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
        max_length=MAX_BASIC_LENGTH
    )
]

DescriptionField = Annotated[
    str,
    Field(
        min_length=MIN_BASIC_LENGTH,
        max_length=MAX_DESCRIPTION_LENGTH,
        description='Description field'
    )
]

PasswordString = Annotated[
    str,
    Field(
        min_length=PASSWORD_MIN_LENGTH,
        max_length=MAX_BASIC_LENGTH
    )
]