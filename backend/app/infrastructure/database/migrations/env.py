from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

from backend.app.infrastructure.database.base import Base
from backend.app.infrastructure.models.events import Event, Category, Location
from backend.app.infrastructure.models.users import User, Profile, Organizer
from backend.app.infrastructure.models import *
print("Starting migration process...")
print("Imported models:")
print("Event:", Event.__table__.name if hasattr(Event, '__table__') else "Not initialized")
print("Category:", Category.__table__.name if hasattr(Category, '__table__') else "Not initialized")
print("Location:", Location.__table__.name if hasattr(Location, '__table__') else "Not initialized")
print("User:", User.__table__.name if hasattr(User, '__table__') else "Not initialized")
print("Profile:", Profile.__table__.name if hasattr(Profile, '__table__') else "Not initialized")
print("Organizer:", Organizer.__table__.name if hasattr(Organizer, '__table__') else "Not initialized")

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


database_url = "postgresql+asyncpg://postgres:postgres@localhost:5432/dev_events"
config.set_main_option(
    'sqlalchemy.url',
    database_url + "?async_fallback=True"
)

target_metadata = Base.metadata
print("\nAll registered tables:", Base.metadata.tables.keys())
print("Number of tables:", len(Base.metadata.tables))
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
