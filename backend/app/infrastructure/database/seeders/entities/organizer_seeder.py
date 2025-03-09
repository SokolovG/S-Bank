from typing import override

from backend.app.infrastructure.database.seeders.base_seeder import BaseSeeder
from backend.app.infrastructure.database.seeders.constants import NUM_TEST_DATA
from backend.app.infrastructure.models import Organizer


class OrganizerSeeder(BaseSeeder):
    @override
    async def run(self) -> None:
        try:
            self.log("Starting organizers seeding...")
            await self.clear_table(Organizer)

            for index in range(1, NUM_TEST_DATA + 1):
                name = self.faker.company()
                organizer = Organizer(
                    user_id=index,
                    verified=self.faker.boolean(),
                    website=self.faker.url(),
                    contact=self.faker.email(),
                    name=name,
                    description=self.faker.paragraph(nb_sentences=4),
                    logo_url=self.faker.image_url(),
                    rating=self.faker.random_int(1, 5),
                )

                self.log(f"Created location - {name} ")
                self.session.add(organizer)

            await self.session.commit()
            self.log("Organizers created successfully!", level="success")

        except Exception as e:
            self.log(f"Error creating organizers: {str(e)}", level="error")
            await self.session.rollback()
