from litestar.plugins.pydantic.dto import PydanticDTO

from backend.src.interfaces.api.schemas import UserCreate, UserRead, UserUpdate


class UserCreateDTO(PydanticDTO[UserCreate]):
    pass

class UserUpdateDTO(PydanticDTO[UserUpdate]):
    pass

class UserReadDTO(PydanticDTO[UserRead]):
    pass

