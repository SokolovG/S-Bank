import random
from datetime import date, timedelta
from typing import override

from sqlalchemy import select

from src.infrastructure.database.models import Account, Card
from src.infrastructure.database.models.enums import CardType
from src.infrastructure.database.seeders.base_seeder import BaseSeeder


class CardSeeder(BaseSeeder):
    @override
    async def run(self) -> None:
        try:
            self.log("Starting cards seeding...")
            await self.clear_table(Card)

            # Получаем существующие счета и пользователей
            account_query = select(Account.id, Account.user_id)
            account_data = (await self.session.execute(account_query)).all()

            if not account_data:
                self.log("No accounts found. Please run AccountSeeder first.", level="error")
                return

            # Создаем карты для счетов
            for account_id, user_id in account_data:
                # Случайно решаем, сколько карт создать для этого счета (0-2)
                num_cards = random.randint(0, 2)

                for _ in range(num_cards):
                    # Генерируем номер карты (только для примера, в реальности используйте алгоритм Луна)
                    card_number = f"{self.faker.random_number(digits=16, fix_len=True)}"

                    # Срок действия (от 1 до 5 лет от текущей даты)
                    years_valid = random.randint(1, 5)
                    exp_date = date.today() + timedelta(days=365 * years_valid)

                    # Хеш CVV (в реальности должен быть надежно зашифрован)
                    cvv = str(random.randint(100, 999))
                    cvv_hash = f"hash_{cvv}"  # Это только для примера!

                    card_type = random.choice(list(CardType))
                    daily_limit = self.faker.pydecimal(min_value=500, max_value=5000, right_digits=2)
                    is_activated = self.faker.boolean(chance_of_getting_true=70)

                    card = Card(
                        card_number=card_number,
                        card_type=card_type,
                        exp_date=exp_date,
                        cvv_hash=cvv_hash,
                        is_activated=is_activated,
                        is_blocked=False,
                        daily_limit=daily_limit,
                        user_id=user_id,
                        account_id=account_id
                    )

                    self.log(f"Created {card_type.value} card for account {account_id}")
                    self.session.add(card)

            await self.session.commit()
            self.log("Cards created successfully!", level="success")

        except Exception as e:
            self.log(f"Error creating cards: {str(e)}", level="error")
            await self.session.rollback()