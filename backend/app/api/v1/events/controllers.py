from __future__ import annotations

from litestar import get, Controller

from backend.app.api.v1.events.dependencies import RepositoryDependencies
from backend.app.infrastructure.schemas.events.event import EventRead


class EventController(Controller):
    """Basic event controller."""

    path = '/events'

    @get()
    async def get_all_events(self, repositories: RepositoryDependencies) -> list[EventRead]:
        """Get all events."""
        event_repo = repositories.get('event_repo')  # Get repo.
        events = await event_repo.list()
        return [EventRead.model_validate(event) for event in events]

    @get('/{event_id:int}')
    async def get_event_by_pk(self, repositories: RepositoryDependencies, event_id: int) -> EventRead:
        """Get event by_pk."""
        event_repo = repositories.get('event_repo')  # Get repo.
        event = await event_repo.get_one_or_none(id=event_id)
        return EventRead.model_validate(event)
