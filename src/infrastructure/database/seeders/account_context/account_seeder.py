import random
from typing import override

from sqlalchemy import select

from src.infrastructure.database.models import Account, UserModel
from src.infrastructure.database.models.enums import AccountType, Currency
from src.infrastructure.database.seeders.base_seeder import NUM_TEST_DATA, BaseSeeder


class AccountSeeder(BaseSeeder):
    @override
    async def run(self) -> None:
        try:
            self.log("Starting accounts seeding...")
            await self.clear_table(Account)

            user_query = select(UserModel.id)
            user_ids = (await self.session.execute(user_query)).scalars().all()

            if not user_ids:
                self.log("No users found. Please run UserSeeder first.", level="error")
                return

            for _ in range(NUM_TEST_DATA):
                account_number = f"ACC{self.faker.random_number(digits=10, fix_len=True)}"
                iban = f"GB{self.faker.random_number(digits=20, fix_len=True)}"
                account_type = random.choice(list(AccountType))  # noqa: S311
                currency = random.choice(list(Currency))  # noqa: S311
                balance = self.faker.pydecimal(min_value=0, max_value=10000, right_digits=2)
                user_id = random.choice(user_ids)  # noqa: S311

                account = Account(
                    account_number=account_number,
                    account_type=account_type,
                    currency=currency,
                    balance=balance,
                    iban=iban,
                    user_id=user_id,
                )

                self.log(f"Created account - {account_number}")
                self.session.add(account)

            await self.session.commit()
            self.log("Accounts created successfully!", level="success")

        except Exception as e:
            self.log(f"Error creating accounts: {str(e)}", level="error")
            await self.session.rollback()
