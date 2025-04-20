import uvicorn
from litestar import Litestar
from litestar.logging import LoggingConfig
from sqladmin import ModelView
from sqladmin_litestar_plugin import SQLAdminPlugin

from src.infrastructure.database.config import get_sqlalchemy_config, get_sqlalchemy_plugin
from src.infrastructure.database.models import Transaction
from src.interfaces.api.user_context.routes import auth_router, user_router
from src.interfaces.cli.commands import CLIPlugin

logging_config = LoggingConfig(
    root={"level": "INFO", "handlers": ["queue_listener"]},
    formatters={
        "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"},
    },
    loggers={
        "src.events": {"level": "DEBUG", "propagate": True},
        "src.users": {"level": "INFO", "propagate": True},
        "src.auth": {"level": "WARNING", "propagate": True},
    },
    log_exceptions="always",
)


class TransactionAdmin(ModelView, model=Transaction):  # type: ignore
    column_list = [Transaction.transaction_type, Transaction.amount, Transaction.currency]


sqlalchemy_plugin = get_sqlalchemy_plugin()
sqlalchemy_config = get_sqlalchemy_config()
admin = SQLAdminPlugin(engine=sqlalchemy_config.get_engine(), base_url="/admin", views=[TransactionAdmin])
app = Litestar(
    route_handlers=[user_router, auth_router],
    plugins=[sqlalchemy_plugin, admin, CLIPlugin()],
    debug=True,
    logging_config=logging_config,
)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
