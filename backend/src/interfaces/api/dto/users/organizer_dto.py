from backend.src.interfaces.api.dto.base_dto import BasePydanticDTO
from backend.src.interfaces.api.schemas import OrganizerCreate, OrganizerRead, OrganizerUpdate


class OrganizerCreateDTO(BasePydanticDTO[OrganizerCreate]):
    pass

class OrganizerUpdateDTO(BasePydanticDTO[OrganizerUpdate]):
    pass

class OrganizerReadDTO(BasePydanticDTO[OrganizerRead]):
    pass

