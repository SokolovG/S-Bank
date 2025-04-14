from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class BaseService(Generic[T], ABC):
    @abstractmethod
    async def get_by_id(self, id: int) -> T | None:
        pass

    @abstractmethod
    async def get_all(self) -> list[T]:
        pass

    @abstractmethod
    async def create(self, data: dict) -> T:
        pass

    @abstractmethod
    async def update(self, id: int, data: dict) -> T | None:
        pass

    @abstractmethod
    async def delete(self, id: int) -> bool:
        pass