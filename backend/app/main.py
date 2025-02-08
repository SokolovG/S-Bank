import uvicorn

from litestar import Litestar
from litestar.contrib.sqlalchemy.plugins import (
    SQLAlchemyPlugin,
    SQLAlchemyAsyncConfig
)

from backend.app.infrastructure.database.base import Base
from backend.app.core.config.settings import settings
from backend.app.api.v1.events.dependencies import dependencies
from backend.app.api.v1.events.routes import event_router


config = SQLAlchemyAsyncConfig(
    connection_string=settings.database_url,
    create_all=True,
    metadata=Base.metadata
)

plugin = SQLAlchemyPlugin(config=config)
app = Litestar(
    route_handlers=[event_router],
    plugins=[plugin],
    debug=True,
    dependencies=dependencies
)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
