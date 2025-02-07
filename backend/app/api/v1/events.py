from litestar import get, Controller
from litestar.di import Provide

from backend.app.models.events import Event
from ...repositories.event import EventRepository, provide_event_repo


class EventController(Controller):
    dependencies = {'event_repo': Provide(provide_event_repo)}
    path = "/events"

    @get()
    async def get_events(self, event_repo: EventRepository) -> list[Event]:
        events = await event_repo.list()
        return events

