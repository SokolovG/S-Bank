import logging
import sys
from typing import Optional, Any
from colorama import init, Fore, Style
from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession


init()


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

        logger.setLevel(logging.INFO)

        if logger.handlers:
            logger.handlers.clear()

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            f'{Fore.GREEN}%(name)s{Style.RESET_ALL} - '
            f'%(message)s',
        )

        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

        return logger

    def log(self, message: str, level: Optional[str] = 'info') -> None:
        """Log messages with specified level and colors."""
        if level == 'info':
            message = f"{Fore.WHITE}{message}{Style.RESET_ALL}"
            self.logger.info(message)
        elif level == 'error':
            message = f"{Fore.RED}{message}{Style.RESET_ALL}"
            self.logger.error(message)
        elif level == 'warning':
            message = f"{Fore.YELLOW}{message}{Style.RESET_ALL}"
            self.logger.warning(message)
        elif level == 'success':
            message = f"{Fore.GREEN}{message}{Style.RESET_ALL}"
            self.logger.info(message)

    def run(self) -> Any:
        """Execute seeding process. Must be implemented by derived classes."""
        raise NotImplementedError('Implement this method in derived class')