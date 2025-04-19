from typing import Final

from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig, SQLAlchemyPlugin

from src.infrastructure.database.base import Base
from src.infrastructure.database.settings import settings

MAX_BASIC_LENGTH: Final[int] = 255
MIN_BASIC_LENGTH: Final[int] = 2
MAX_DESCRIPTION_LENGTH: Final[int] = 1000
PASSWORD_MIN_LENGTH: Final[int] = 8


def get_sqlalchemy_config() -> SQLAlchemyAsyncConfig:
    """Get SQLAlchemy config."""
    return SQLAlchemyAsyncConfig(connection_string=settings.database_url, create_all=True, metadata=Base.metadata)


def get_sqlalchemy_plugin() -> SQLAlchemyPlugin:
    """Get SQLAlchemy plugin."""
    return SQLAlchemyPlugin(config=get_sqlalchemy_config())
