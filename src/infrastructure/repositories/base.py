from typing import Generic, TypeVar

from litestar.plugins.sqlalchemy import repository

T = TypeVar("T")


class BasicRepository(repository.SQLAlchemyAsyncRepository[T], Generic[T]):
    """Base repository providing common functionality for all repositories."""
