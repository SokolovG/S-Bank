"""Module for event controller.

Contains the following routes:
    - GET /events
"""

from litestar import get, Controller

from backend.app.domain.models.events import Event


class EventController(Controller):
    """Basic event controller.

    Contains dependencies with EventRepository
    """
    path = "/events"

    @get()
    async def get_events(self, repositories: dict) -> list[Event]:
        event_repo = repositories['event_repo']
        events = await event_repo.list()
        return events

