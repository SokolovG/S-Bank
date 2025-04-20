from src.domain.user_context.events.user_events import UserRegisteredEvent


class UserRegisteredHandler:
    def handle(self, event: UserRegisteredEvent) -> None:
        """Обработать событие регистрации пользователя."""
        msg = f"Пользователь зарегистрирован:{event.email} с ID {event.user_id} в {event.timestamp}"
        print(msg)
