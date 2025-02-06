import uvicorn

from litestar import Litestar
from litestar.contrib.sqlalchemy.plugins import (
    SQLAlchemyPlugin,
    SQLAlchemyAsyncConfig
)

from backend.app.database.connection import Base

# Bas
from .config.settings import settings


config = SQLAlchemyAsyncConfig(
    connection_string=settings.database_url,
    create_all=True,
    metadata=Base.metadata
)

plugin = SQLAlchemyPlugin(config=config)
app = Litestar(
    route_handlers=[],
    plugins=[plugin],
    debug=True
)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
