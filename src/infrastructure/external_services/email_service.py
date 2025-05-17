class EmailService:
    def __init__(self, smtp_host: str, smtp_port: int, username: str, password: str) -> None:
        """Отправляет email с кодом подтверждения."""
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_verification_email(self, email: str, code: str) -> None:
        """Отправляет email с кодом подтверждения."""
