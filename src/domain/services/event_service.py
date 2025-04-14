from src.domain.services.base_service import BaseService
from src.infrastructure.database.models.event_model import Event
from src.infrastructure.repositories.event import EventRepository


class EventService(BaseService[Event]):
    def __init__(self, repository: EventRepository):
        self.repository = repository

    async def get_by_id(self, id: int) -> Event | None:
        return await self.repository.get_one_or_none(id=id)

    async def get_all(self) -> list[Event]:
        return await self.repository.list()

    async def create(self, data: dict) -> Event:
        return await self.repository.add(Event(**data))

    async def update(self, id: int, data: dict) -> Event | None:
        event = await self.get_by_id(id)
        if not event:
            return None

        # Обновите атрибуты
        for key, value in data.items():
            if hasattr(event, key):
                setattr(event, key, value)

        await self.repository.update(event)
        return event

    async def delete(self, id: int) -> bool:
        event = await self.get_by_id(id)
        if not event:
            return False
        await self.repository.delete(event)
        return True

    async def search_events(self, filters: dict) -> list[Event]:
        pass

    async def register_participant(self, event_id: int, profile_id: int) -> bool:
        pass