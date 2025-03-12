import asyncio

import click
import uvicorn
from click import Group
from litestar import Litestar
from litestar.config.cors import CORSConfig
from litestar.logging import LoggingConfig
from litestar.plugins import CLIPluginProtocol
from sqladmin import ModelView
from sqladmin_litestar_plugin import SQLAdminPlugin

from backend.app.api.v1.events.routes import event_router
from backend.app.infrastructure.database.config import (
    get_sqlalchemy_plugin,
    get_sqlalchemy_config,
)
from backend.app.infrastructure.database.seeders.run_seeder import run
from backend.app.infrastructure.models import Event

cors_config = CORSConfig(
    allow_origins=["http://localhost:5173"],
    allow_methods=['*'],
    allow_headers=['*']
)

class CLIPlugin(CLIPluginProtocol):
    def on_cli_init(self, cli: Group) -> None:
        @cli.command()
        def run_seeders():
            asyncio.run(run())
            click.echo("Seeders executed successfully!")

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

sqlalchemy_plugin = get_sqlalchemy_plugin()
sqlalchemy_config = get_sqlalchemy_config()
admin = SQLAdminPlugin(engine=sqlalchemy_config.get_engine(), base_url="/admin", views=[EventAdmin])
app = Litestar(
    route_handlers=[event_router],
    plugins=[sqlalchemy_plugin, admin, CLIPlugin()],
    debug=True,
    cors_config=cors_config,
    logging_config=logging_config
)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)