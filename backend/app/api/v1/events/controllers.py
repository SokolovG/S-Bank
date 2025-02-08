"""Module for event controller.

Contains the following routes:
    - GET /events
"""

from litestar import get, Controller
from litestar.di import Provide

from backend.app.domain.models.events import Event
from backend.app.domain.repositories.event import EventRepository, provide_event_repo


class EventController(Controller):
    """Basic event controller.

    Contains dependencies with EventRepository
    """
    dependencies = {'event_repo': Provide(provide_event_repo)}
    path = "/events"

    @get()
    async def get_events(self, event_repo: EventRepository) -> list[Event]:
        events = await event_repo.list()
        return events

