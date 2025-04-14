from typing import TypeVar

from litestar.plugins.pydantic.dto import PydanticDTO

T = TypeVar('T')

class BasePydanticDTO(PydanticDTO[T]):
    pass