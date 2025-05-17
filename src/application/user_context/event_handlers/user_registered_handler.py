from logging import getLogger

from src.application.user_context.services import VerificationService
from src.domain.user_context.events.user_events import UserRegisteredEvent
from src.infrastructure.external_services import EmailService


class UserRegisteredHandler:
    def __init__(self, email_service: EmailService, verification_service: VerificationService) -> None:
        """F."""
        self.email_service = email_service
        self.verification_repository = verification_service
        self.logger = getLogger(__name__)

    def handle(self, event: UserRegisteredEvent) -> None:
        """Обработать событие регистрации пользователя."""
        verification_code = self._generate_verification_code()

        # Сохранение кода для проверки позже
        self.verification_repository.save_code(user_id=event.user_id, code=verification_code)

        # Отправка письма с кодом
        self.email_service.send_verification_email(email=event.email, code=verification_code)

        self.logger.info(f"Пользователь зарегистрирован: {event.email} с ID {event.user_id} в {event.timestamp}")
        self.logger.info(f"Отправлен код подтверждения на {event.email}")

    def _generate_verification_code(self) -> str:
        return "123456"  # Заглушка
