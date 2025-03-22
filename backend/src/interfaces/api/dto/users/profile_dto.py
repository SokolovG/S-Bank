from backend.src.interfaces.api.dto.base_dto import BasePydanticDTO
from backend.src.interfaces.api.schemas import ProfileCreate, ProfileRead, ProfileUpdate


class ProfileCreateDTO(BasePydanticDTO[ProfileCreate]):
    pass

class ProfileUpdateDTO(BasePydanticDTO[ProfileUpdate]):
    pass

class ProfileReadDTO(BasePydanticDTO[ProfileRead]):
    pass

