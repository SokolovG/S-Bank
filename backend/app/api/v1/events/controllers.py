from __future__ import annotations

from litestar import get, Controller

from backend.app.infrastructure.schemas.events.event import EventRead


class EventController(Controller):
    """Basic event controller.

    Contains dependencies with EventRepository
    Routes:
        - GET /events
        - GET /events/{event_id}
    """

    path = '/events'

    @get()
    async def get_all_events(self, repositories: dict) -> list[EventRead]:
        """Get all events.

        - GET /events
        """
        event_repo = repositories.get('event_repo')  # Get repo.
        events = await event_repo.list()
        return events

    @get('/{event_id:int}')
    async def get_event_by_pk(self,
                              repositories: dict,
                              event_id: int) -> EventRead:
        """Get event by_pk.

        - GET /events/{event_id}
        """
        event_repo = repositories.get('event_repo')  # Get repo.
        event = await event_repo.get_one_or_none(id=event_id)
        return event
