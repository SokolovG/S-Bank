from typing import Any

from sqlalchemy import delete

from backend.app.infrastructure.database.seeders.base_seeder import BaseSeeder
from backend.app.infrastructure.database.seeders.constants import categories
from backend.app.infrastructure.models.categories import Category



class CategorySeeder(BaseSeeder):
    async def run(self) -> Any:
        try:
            self.log('Starting category seeding...')

            await self.session.execute(delete(Category))
            self.log('Cleared existing categories')

            for category_name in categories:
                category = Category(
                    name=category_name,
                    slug=self.faker.slug(),
                    description=self.faker.text()
                )
                self.log(f'Created category - {category_name}')
                self.session.add(category)

            await self.session.commit()
            self.log('Categories created successfully!', level='success')

        except Exception as e:
            self.log(f'Error creating categories: {str(e)}', level='error')
            await self.session.rollback()
            return f'Error seeding categories: {e}'

