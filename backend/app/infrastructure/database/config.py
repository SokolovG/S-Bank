from litestar.contrib.sqlalchemy.plugins import (
    SQLAlchemyPlugin,
    SQLAlchemyAsyncConfig,
)

from backend.app.core.config.settings import settings
from backend.app.infrastructure.database.base import Base


def get_sqlalchemy_config() -> SQLAlchemyAsyncConfig:
    """Get SQLAlchemy config."""
    return SQLAlchemyAsyncConfig(
        connection_string=settings.database_url,
        create_all=True,
        metadata=Base.metadata
    )

def get_sqlalchemy_plugin() -> SQLAlchemyPlugin:
    """Get SQLAlchemy plugin."""
    return SQLAlchemyPlugin(config=get_sqlalchemy_config())