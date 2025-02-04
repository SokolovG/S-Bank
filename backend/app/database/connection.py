from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from backend.app.config.settings import settings


# Base class for models.
class Base(DeclarativeBase):
    pass


# Database main engine.
engine = create_async_engine(
    url=settings.database_url,
    echo=True # Show SQL query.
)

# Session fabric.
async_session = async_sessionmaker(
    engine,
    class_=AsyncSession, # Sessions will async.
    expire_on_commit=False
)

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session