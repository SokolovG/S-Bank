from typing import Any

from backend.app.infrastructure.database.seeders.base_seeder import BaseSeeder
from backend.app.infrastructure.database.seeders.constants import categories
from backend.app.infrastructure.models.categories import Category



class CategorySeeder(BaseSeeder):
    async def run(self) -> Any:
        try:
            self.log(f'Lets start creating test categories...')
            for category_name in categories:
                category = Category(
                    name=category_name,
                    slug=self.faker.slug(),
                    description=self.faker.text()
                )
                self.log(f'Created category - {category_name}')
                self.session.add(category)
                self.log('Events created successfully!', level='success')

                await self.session.commit()

        except Exception as e:
            self.logger(f'Error creating events: {str(e)}', level='error')
            await self.session.rollback()

            return f'Error seeding categories: {e}'

