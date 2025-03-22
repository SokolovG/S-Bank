from litestar.plugins.pydantic.dto import PydanticDTO

from backend.src.interfaces.api.schemas import CategoryCreate, CategoryRead, CategoryUpdate


class CategoryCreateDTO(PydanticDTO[CategoryCreate]):
    pass

class CategoryUpdateDTO(PydanticDTO[CategoryUpdate]):
    pass

class CategoryReadDTO(PydanticDTO[CategoryRead]):
    pass

