import uvicorn
from litestar import Litestar
from litestar.config.cors import CORSConfig
from litestar.contrib.sqlalchemy.plugins import (
    SQLAlchemyPlugin,
    SQLAlchemyAsyncConfig,
)
from litestar.logging import LoggingConfig
from sqladmin import ModelView
from sqladmin_litestar_plugin import SQLAdminPlugin

from backend.app.api.v1.events.routes import event_router
from backend.app.core.config.settings import settings
from backend.app.infrastructure.database.base import Base
from backend.app.infrastructure.models import Event

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

logging_config = LoggingConfig(
    root={"level": "INFO", "handlers": ["queue_listener"]},
    formatters={
        "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"},
    },
    loggers={
        "app.events": {"level": "DEBUG", "propagate": True},
        "app.users": {"level": "INFO", "propagate": True},
        "app.auth": {"level": "WARNING", "propagate": True},
    },
    log_exceptions="always",
)

class EventAdmin(ModelView, model=Event):
    column_list = [Event.name, Event.price, Event.description]

sqlalchemy_plugin = SQLAlchemyPlugin(config=config)
admin = SQLAdminPlugin(engine=config.get_engine(), base_url="/admin", views=[EventAdmin])
app = Litestar(
    route_handlers=[event_router],
    plugins=[sqlalchemy_plugin, admin],
    debug=True,
    cors_config=cors_config,
    logging_config=logging_config
)

if __name__ == '__main__':
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)