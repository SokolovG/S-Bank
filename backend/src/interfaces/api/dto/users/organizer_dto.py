from litestar.plugins.pydantic.dto import PydanticDTO

from backend.src.interfaces.api.schemas import OrganizerCreate, OrganizerRead, OrganizerUpdate


class OrganizerCreateDTO(PydanticDTO[OrganizerCreate]):
    pass

class OrganizerUpdateDTO(PydanticDTO[OrganizerUpdate]):
    pass

class OrganizerReadDTO(PydanticDTO[OrganizerRead]):
    pass

