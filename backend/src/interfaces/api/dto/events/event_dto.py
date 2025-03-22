from backend.src.interfaces.api.dto.base_dto import BasePydanticDTO
from backend.src.interfaces.api.schemas import EventCreate, EventRead, EventUpdate


class EventCreateDTO(BasePydanticDTO[EventCreate]):
    pass


class EventUpdateDTO(BasePydanticDTO[EventUpdate]):
    pass

class EventReadDTO(BasePydanticDTO[EventRead]):
    pass
