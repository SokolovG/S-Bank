from litestar.plugins.pydantic.dto import PydanticDTO

from backend.src.interfaces.api.schemas import ProfileCreate, ProfileRead, ProfileUpdate


class ProfileCreateDTO(PydanticDTO[ProfileCreate]):
    pass

class ProfileUpdateDTO(PydanticDTO[ProfileUpdate]):
    pass

class ProfileReadDTO(PydanticDTO[ProfileRead]):
    pass

