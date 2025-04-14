from src.interfaces.api.dto.base_dto import BasePydanticDTO
from src.interfaces.api.schemas import LocationCreate, LocationRead, LocationUpdate


class LocationCreateDTO(BasePydanticDTO[LocationCreate]):
    pass


class LocationUpdateDTO(BasePydanticDTO[LocationUpdate]):
    pass

class LocationReadDTO(BasePydanticDTO[LocationRead]):
    pass
