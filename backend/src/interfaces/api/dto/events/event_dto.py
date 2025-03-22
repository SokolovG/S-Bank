from litestar.plugins.pydantic.dto import PydanticDTO

from backend.src.interfaces.api.schemas import EventCreate, EventRead, EventUpdate


class EventCreateDTO(PydanticDTO[EventCreate]):
    pass


class EventUpdateDTO(PydanticDTO[EventUpdate]):
    pass

class EventReadDTO(PydanticDTO[EventRead]):
    pass
