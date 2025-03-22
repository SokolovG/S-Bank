from backend.src.interfaces.api.dto.base_dto import BasePydanticDTO
from backend.src.interfaces.api.schemas import CategoryCreate, CategoryRead, CategoryUpdate


class CategoryCreateDTO(BasePydanticDTO[CategoryCreate]):
    pass

class CategoryUpdateDTO(BasePydanticDTO[CategoryUpdate]):
    pass

class CategoryReadDTO(BasePydanticDTO[CategoryRead]):
    pass

