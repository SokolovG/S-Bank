from logging import getLogger
from typing import TYPE_CHECKING

from src.domain.user_context.events.user_events import UserVerifiedEvent
from src.domain.user_context.repositories_interfaces import IUserStatisticsRepository

if TYPE_CHECKING:
    from src.domain.user_context.repositories_interfaces import (
        IUserStatisticsRepository,
    )


class UserVerifiedHandler:
    def __init__(self, stats_repository: IUserStatisticsRepository) -> None:
        """F."""
        self.stats_repository = stats_repository
        self.logger = getLogger(__name__)

    def handle(self, event: UserVerifiedEvent) -> None:
        """Обновляет статистику после подтверждения регистрации пользователя."""
        self.stats_repository.increment_verified_users_count()
        self.logger.info(f"Статистика обновлена: пользователь {event.user_id} подтвержден")
