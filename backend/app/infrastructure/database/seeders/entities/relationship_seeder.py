import random
from typing import Any

from sqlalchemy import delete, select

from backend.app.infrastructure.database.seeders.base_seeder import BaseSeeder
from backend.app.infrastructure.models import Event, Profile, EventRegistration


class RelationshipSeeder(BaseSeeder):
    async def run(self) -> Any:
        try:
            self.log('Starting relationships seeding...')
            await self.session.execute(delete(EventRegistration))
            self.log('Cleared existing relationships')

            profiles = (await self.session.execute(
                select(Profile)
            )).scalars().all()

            events = (await self.session.execute(
                select(Event)
            )).scalars().all()

            for profile in profiles:
                num_events = random.randint(1, 3)
                selected_events = random.sample(events, num_events)
                profile.registered_events.extend(selected_events)

            await self.session.commit()
            self.log('Relationships created successfully!', level='success')



        except Exception as e:
            self.log(f'Error creating relationships: {str(e)}', level='error')
            await self.session.rollback()