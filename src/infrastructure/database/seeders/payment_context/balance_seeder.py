from typing import override

from sqlalchemy import select

from src.infrastructure.database.models import Account, Balance
from src.infrastructure.database.seeders.base_seeder import BaseSeeder


class BalanceSeeder(BaseSeeder):
    @override
    async def run(self) -> None:
        try:
            self.log("Starting balances seeding...")
            await self.clear_table(Balance)

            account_query = select(Account.id)
            account_ids = (await self.session.execute(account_query)).scalars().all()

            if not account_ids:
                self.log("No accounts found. Please run AccountSeeder first.", level="error")
                return

            # Типы балансов
            balance_types = ["available", "pending", "reserved"]

            # Для каждого счета создаем все типы балансов
            for account_id in account_ids:
                for balance_type in balance_types:
                    # Главный баланс - "available", остальные меньше
                    if balance_type == "available":
                        amount = self.faker.pydecimal(min_value=100, max_value=10000, right_digits=2)
                    else:
                        amount = self.faker.pydecimal(min_value=0, max_value=500, right_digits=2)

                    balance = Balance(
                        account_id=account_id,
                        balance_type=balance_type,
                        amount=amount
                    )

                    self.log(f"Created {balance_type} balance for account {account_id}")
                    self.session.add(balance)

            await self.session.commit()
            self.log("Balances created successfully!", level="success")

        except Exception as e:
            self.log(f"Error creating balances: {str(e)}", level="error")
            await self.session.rollback()