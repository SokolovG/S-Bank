from src.interfaces.api.dto.base_dto import BasePydanticDTO
from src.interfaces.api.schemas import CategoryCreate, CategoryRead, CategoryUpdate


class CategoryCreateDTO(BasePydanticDTO[CategoryCreate]):
    pass

class CategoryUpdateDTO(BasePydanticDTO[CategoryUpdate]):
    pass

class CategoryReadDTO(BasePydanticDTO[CategoryRead]):
    pass

