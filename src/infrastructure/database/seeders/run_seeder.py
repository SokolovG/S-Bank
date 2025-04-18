import asyncio

from src.infrastructure.database.config import get_sqlalchemy_config
from src.infrastructure.database.seeders.user_context import UserSeeder
from src.infrastructure.database.seeders.account_context import AccountSeeder
from src.infrastructure.database.seeders.payment_context import CardSeeder, BalanceSeeder
from src.infrastructure.database.seeders.transaction_context import TransactionSeeder

sqlalchemy_config = get_sqlalchemy_config()


async def run() -> None:
    """Run all seeders."""
    session_maker = sqlalchemy_config.create_session_maker()
    async with session_maker() as session:
        seeders = [
            UserSeeder(session=session),
            AccountSeeder(session=session),
            BalanceSeeder(session=session),
            CardSeeder(session=session),
            TransactionSeeder(session=session),
        ]
        for seeder in seeders:
            await seeder.run()


if __name__ == "__main__":
    asyncio.run(run())
