import secrets
from datetime import datetime, timedelta
from typing import override

from sqlalchemy import select

from src.infrastructure.database.models import Account, Transaction
from src.infrastructure.database.models.enums import TransactionStatus, TransactionType
from src.infrastructure.database.seeders.base_seeder import NUM_TEST_DATA, BaseSeeder


class TransactionSeeder(BaseSeeder):
    @override
    async def run(self) -> None:
        try:
            self.log("Starting transactions seeding...")
            await self.clear_table(Transaction)

            account_query = select(Account.id, Account.currency)
            accounts = (await self.session.execute(account_query)).all()

            if not accounts:
                self.log("No accounts found. Please run AccountSeeder first.", level="error")
                return

            account_map = {acc_id: currency for acc_id, currency in accounts}
            account_ids = list(account_map.keys())

            for _ in range(NUM_TEST_DATA):
                source_account_id = secrets.choice(account_ids)
                source_currency = account_map[source_account_id]

                transaction_type = secrets.choice(list(TransactionType))

                if transaction_type in [
                    TransactionType.TRANSFER,
                    TransactionType.INTERNATIONAL_TRANSFER,
                ]:
                    other_accounts = [acc for acc in account_ids if acc != source_account_id]
                    if other_accounts and secrets.randbelow(2) == 0:
                        destination_account_id = secrets.choice(other_accounts)
                        recipient_name = None
                        recipient_iban = None
                        swift_code = None
                    else:
                        destination_account_id = None
                        recipient_name = self.faker.name()
                        recipient_iban = f"GB{self.faker.random_number(digits=20, fix_len=True)}"
                        swift_code = self.faker.lexify(text="????GB??").upper()
                else:
                    destination_account_id = None
                    recipient_name = None
                    recipient_iban = None
                    swift_code = None

                status = secrets.choice(list(TransactionStatus))

                amount = self.faker.pydecimal(min_value=1, max_value=1000, right_digits=2)

                transaction_date = self.faker.date_time_between(start_date="-30d", end_date="now")

                if status in [
                    TransactionStatus.COMPLETED,
                    TransactionStatus.FAILED,
                    TransactionStatus.REJECTED,
                ]:
                    processed_date = transaction_date + timedelta(minutes=secrets.randbelow(60) + 1)
                else:
                    processed_date = None

                transaction = Transaction(
                    transaction_type=transaction_type,
                    amount=amount,
                    currency=source_currency,
                    status=status,
                    description=self.faker.sentence(),
                    source_account_id=source_account_id,
                    destination_account_id=destination_account_id,
                    recipient_name=recipient_name,
                    recipient_iban=recipient_iban,
                    swift_code=swift_code,
                    transaction_date=transaction_date,
                    processed_date=processed_date or datetime.now(),
                )

                self.log(f"Created {transaction_type} transaction for account {source_account_id}")
                self.session.add(transaction)

            await self.session.commit()
            self.log("Transactions created successfully!", level="success")

        except Exception as e:
            self.log(f"Error creating transactions: {str(e)}", level="error")
            await self.session.rollback()
