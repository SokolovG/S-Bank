from typing import override

from backend.app.infrastructure.database.seeders.base_seeder import BaseSeeder
from backend.app.infrastructure.database.seeders.constants import locations
from backend.app.infrastructure.models import Location


class LocationSeeder(BaseSeeder):
    @override
    async def run(self) -> None:
        try:
            self.log("Starting locations seeding...")
            await self.clear_table(Location)

            for location_name in locations:
                location = Location(
                    name=location_name,
                    address=self.faker.address(),
                    city=self.faker.city(),
                    country=self.faker.country(),
                )

                self.log(f"Created location - {location_name}")
                self.session.add(location)

            await self.session.commit()
            self.log("Locations created successfully!", level="success")

        except Exception as e:
            self.log(f"Error creating categories: {str(e)}", level="error")
            await self.session.rollback()
