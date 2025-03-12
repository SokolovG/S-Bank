from typing import override

from backend.src.infrastructure.database.models.category_model import Category
from backend.src.infrastructure.database.seeders.base_seeder import BaseSeeder
from backend.src.infrastructure.database.seeders.constants import categories


class CategorySeeder(BaseSeeder):
    @override
    async def run(self) -> None:
        """Category seeder run."""
        try:
            self.log("Starting category seeding...")
            await self.clear_table(Category)

            for category_name in categories:
                category = Category(
                    name=category_name,
                    slug=self.faker.slug(),
                    description=self.faker.text(),
                )
                self.log(f"Created category - {category_name}")
                self.session.add(category)

            await self.session.commit()
            self.log("Categories created successfully!", level="success")

        except Exception as e:
            self.log(f"Error creating categories: {str(e)}", level="error")
            await self.session.rollback()
