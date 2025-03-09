from litestar import Litestar
from litestar.config.cors import CORSConfig
from litestar.contrib.sqlalchemy.plugins import (
    SQLAlchemyPlugin,
    SQLAlchemyAsyncConfig,
)

from backend.app.api.v1.events.dependencies import dependencies
from backend.app.api.v1.events.routes import event_router
from backend.app.core.config.settings import settings
from backend.app.infrastructure.database.base import Base

cors_config = CORSConfig(
    allow_origins=["http://localhost:5173"],
    allow_methods=['*'],
    allow_headers=['*']
)
config = SQLAlchemyAsyncConfig(
    connection_string=settings.database_url,
    create_all=True,
    metadata=Base.metadata
)

sqlalchemy_plugin = SQLAlchemyPlugin(config=config)
app = Litestar(
    route_handlers=[event_router],
    plugins=[sqlalchemy_plugin],
    debug=True,
    dependencies=dependencies,
    cors_config=cors_config
)
