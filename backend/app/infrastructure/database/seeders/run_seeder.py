import asyncio

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from backend.app.main import plugin
from backend.app.infrastructure.database.seeders.category_seeder import CategorySeeder
from backend.app.core.config.settings import settings


async def create_session() -> AsyncSession:
    engine = create_async_engine(
        settings.database_url,
        echo=False
    )

    async_session = sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    return async_session()

async def run():
    async with await create_session() as session:
        category_seeder = CategorySeeder(session=session)
        await category_seeder.run()


if __name__ == '__main__':
    # To run - python -m backend.app.infrastructure.database.seeders.run_seeder
    asyncio.run(run())