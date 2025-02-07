import uvicorn

from litestar import Litestar
from litestar.contrib.sqlalchemy.plugins import (
    SQLAlchemyPlugin,
    SQLAlchemyAsyncConfig
)

from backend.app.database.connection import Base
from backend.app.api.v1.events import EventController

# Bas
from .config.settings import settings


config = SQLAlchemyAsyncConfig(
    connection_string=settings.database_url,
    create_all=True,
    metadata=Base.metadata
)

plugin = SQLAlchemyPlugin(config=config)
app = Litestar(
    route_handlers=[EventController],
    plugins=[plugin],
    debug=True
)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
