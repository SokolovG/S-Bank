from litestar.plugins.pydantic.dto import PydanticDTO

from backend.src.interfaces.api.schemas import LocationCreate, LocationRead, LocationUpdate


class LocationCreateDTO(PydanticDTO[LocationCreate]):
    pass


class LocationUpdateDTO(PydanticDTO[LocationUpdate]):
    pass

class LocationReadDTO(PydanticDTO[LocationRead]):
    pass
