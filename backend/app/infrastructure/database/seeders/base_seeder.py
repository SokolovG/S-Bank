from faker import Faker
from typing import Any, Optional
import logging

from sqlalchemy.ext.asyncio import AsyncSession


class BaseSeeder:
    """Base class seeder, defines logging and faker."""

    def __init__(self, session: AsyncSession):
        """Initialize seeder with database session, faker instance and logger."""
        self.session = session
        self.faker = Faker('en-US')
        self.logger = self._setup_logger()

    def _setup_logger(self) -> logging.Logger:
        """Create and configure logger instance for the seeder class."""
        logger = logging.getLogger(self.__class__.__name__)
        return logger

    def log(self, message: str, level: Optional[str] = 'info') -> None:
        """Log messages with specified level (info, error, warning, or success)."""
        if level == 'info':
            self.logger.info(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'success':
            self.logger.info(f"\033[92m{message}\033[0m")

    def run(self) -> Any:
        """Execute seeding process. Must be implemented by derived classes."""
        raise NotImplementedError('Implement this method in derived class')
