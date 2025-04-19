from litestar.di import Provide
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.repositories.user_context.user_repository import UserRepository


async def provide_user_repo(db_session: AsyncSession) -> UserRepository:
    """Provide User repository instance.

    Args:
       db_session: Async database session
    Returns:
       UserRepository instance

    """
    return UserRepository(session=db_session)


user_dependencies = {"repo": Provide(provide_user_repo)}
