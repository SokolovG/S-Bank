from litestar.di import Provide
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.user_context.event_handlers.user_registered_handler import (
    UserRegisteredHandler,
)
from src.application.user_context.services.auth_service import AuthService
from src.common.event_bus import EventBus
from src.domain.user_context.events.user_events import UserRegisteredEvent
from src.infrastructure.repositories.user_context.user_repository import UserRepository


async def provide_user_repo(db_session: AsyncSession) -> UserRepository:
    """Provide User repository instance.

    Args:
       db_session: Async database session
    Returns:
       UserRepository instance

    """
    return UserRepository(db_session=AsyncSession)


async def provide_event_bus() -> EventBus:
    """Provide event bus with registered handlers."""
    event_bus = EventBus()

    # Создаем обработчик
    user_registered_handler = UserRegisteredHandler()

    # Подписываем обработчик на событие
    event_bus.subscribe(UserRegisteredEvent, user_registered_handler.handle)

    return event_bus


async def provide_auth_service(db_session: AsyncSession) -> AuthService:
    """Provide auth service with all dependencies."""
    user_repo = await provide_user_repo(db_session)
    event_bus = await provide_event_bus()
    k = ""
    return AuthService(user_repository=user_repo, secret_key=k, event_bus=event_bus)


user_dependencies = {"auth_service": Provide(provide_auth_service)}
