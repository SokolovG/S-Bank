from typing import Protocol


class IUserStatisticsRepository(Protocol):
    def increment_verified_users_count(self) -> None:
        """Увеличивает счетчик подтвержденных пользователей."""

    def get_verified_users_count(self) -> int:
        """Возвращает количество подтвержденных пользователей."""
