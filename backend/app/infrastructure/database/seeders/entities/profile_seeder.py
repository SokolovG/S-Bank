import random
from typing import Any

from sqlalchemy import delete, select

from backend.app.infrastructure.database.seeders.base_seeder import BaseSeeder
from backend.app.infrastructure.database.seeders.constants import NUM_TEST_DATA
from backend.app.infrastructure.models import Profile, Category


class ProfileSeeder(BaseSeeder):
    async def run(self) -> Any:
        try:
            self.log('Starting profiles seeding...')
            await self.session.execute(delete(Profile))
            self.log('Cleared existing profiles')

            query = select(Category)
            res = await self.session.execute(query)
            categories = res.scalars().all()

            for _ in range(NUM_TEST_DATA):
                first_name = self.faker.first_name()
                random_category = random.choice(categories)
                profile = Profile(
                    user_id=self.faker.random_int(min=1, max=10),
                    first_name=first_name,
                    last_name=self.faker.last_name(),
                    avatar_url=self.faker.image_url(),
                    interested_technologies=Category.name,
                    location=self.faker.country(),
                    birth_date=self.faker.date_of_birth(),
                    gender=self.faker.passport_gender(),
                )

                self.log(f'Created location - {first_name}')
                self.session.add(profile)

            await self.session.commit()
            self.log('Profiles created successfully!', level='success')



        except Exception as e:
            self.log(f'Error creating profiles: {str(e)}', level='error')
            await self.session.rollback()