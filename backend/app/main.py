import uvicorn

from litestar import Litestar
from litestar.contrib.sqlalchemy.plugins import (
    SQLAlchemyPlugin,
    SQLAlchemyAsyncConfig
)

from backend.app.infrastructure.database.base import Base
from backend.app.api.v1.events.controllers import EventController
from backend.app.core.config.settings import settings
from backend.app.api.v1.events.dependencies import dependencies


config = SQLAlchemyAsyncConfig(
    connection_string=settings.database_url,
    create_all=True,
    metadata=Base.metadata
)

plugin = SQLAlchemyPlugin(config=config)
app = Litestar(
    route_handlers=[EventController],
    plugins=[plugin],
    debug=True,
    dependencies=dependencies
)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
