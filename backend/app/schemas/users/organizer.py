from datetime import datetime
from typing import Optional

from pydantic import BaseModel, condecimal

from ..types import BasicString, DescriptionField


class OrganizerRead(BaseModel):
    id: int
    # Foreign Keys.
    # user_id: UserRead
    # Bool fields.
    verified: bool
    # Date fields.
    created_at: datetime
    # String fields.
    website: BasicString
    contact: BasicString
    name: BasicString
    description: DescriptionField
    # Numeric fields
    number_of_events: int
    rating: Optional[condecimal(max_digits=10, decimal_places=2)] = None
