import random

from sqlalchemy import select

from backend.app.infrastructure.database.seeders.base_seeder import BaseSeeder
from backend.app.infrastructure.database.seeders.constants import NUM_TEST_DATA
from backend.app.infrastructure.models import Profile, Category
from backend.app.infrastructure.models.enums import Gender


class ProfileSeeder(BaseSeeder):
    async def run(self) -> None:
        try:
            self.log("Starting profiles seeding...")
            await self.clear_table(Profile)

            query = select(Category)
            res = await self.session.execute(query)
            categories = res.scalars().all()
            category_names = [category.name for category in categories]

            for index in range(NUM_TEST_DATA):
                first_name = self.faker.first_name()
                random_category = random.choice(category_names)
                profile = Profile(
                    user_id=index,
                    first_name=first_name,
                    last_name=self.faker.last_name(),
                    avatar_url=self.faker.image_url(),
                    interested_technologies=random_category,
                    location=self.faker.country(),
                    birth_date=self.faker.date_of_birth(),
                    gender=random.choice(list(Gender)),
                )

                self.log(f"Created profile - {first_name}")
                self.session.add(profile)

            await self.session.commit()
            self.log("Profiles created successfully!", level="success")

        except Exception as e:
            self.log(f"Error creating profiles: {str(e)}", level="error")
            await self.session.rollback()
