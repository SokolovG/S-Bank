from datetime import datetime

from backend.src.interfaces.api.schemas.base_dto import BasePydanticModel
from backend.src.interfaces.api.schemas.custom_types import BasicString


class LocationBase(BasePydanticModel):
    """Base Pydantic schema for Location model.

    This class serves as a foundation for all Location-related schemas.
    All derived schemas inherit these base fields:
    - name: Name of the location/venue
    - address: Street address
    - city: City name
    - country: Country name

    Used as a parent class for:
    - LocationRead: For retrieving location data
    - LocationCreate: For creating new locations
    - LocationUpdate: For updating existing locations
    """

    name: BasicString
    address: BasicString
    city: BasicString
    country: BasicString


class LocationRead(LocationBase):
    """Schema for reading location data."""

    id: int
    created_at: datetime


class LocationCreate(LocationBase):
    """Schema for creating new locations.

    Inherits all fields from LocationBase without modifications.
    """


class LocationUpdate(LocationBase):
    """Schema for updating existing locations.

    Notes:
    - All fields are optional to allow partial updates
    - Only changed fields need to be included in request
    - Inheritance ensures consistent validation rules

    """

    name: BasicString | None = None
    address: BasicString | None = None
    city: BasicString | None = None
    country: BasicString | None = None
