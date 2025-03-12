from __future__ import annotations

from logging import Logger

from litestar import get, Controller

from backend.src.infrastructure.dependencies.dependencies import event_dependencies
from backend.src.infrastructure.repositories.event import EventRepository
from backend.src.interfaces.api.schemas.events.event import EventRead


class EventController(Controller):
    """Basic event controller."""

    path = "/events"
    dependencies = event_dependencies

    @get()
    async def get_all_events(self, repo: EventRepository, logger: Logger) -> list[EventRead]:
        """Get all events."""
        logger.info('Get all events')
        events = await repo.list()
        return [EventRead.model_validate(event) for event in events]

    @get("/{event_id:int}")
    async def get_event_by_pk(self, event_id: int, repo: EventRepository, logger: Logger) -> EventRead:
        """Get event by_pk."""
        logger.info(f"Getting event with id {event_id}")
        event = await repo.get_one_or_none(id=event_id)
        return EventRead.model_validate(event)
