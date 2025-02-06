from litestar import get, Controller
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.events import Event


class EventController(Controller):
    path = "/events"

    @get()
    async def get_events(self, db_session: AsyncSession) -> list[Event]:
        query = select(Event)
        result = await db_session.execute(query)
        events = result.scalars().all()
        return events

    @get('/{event_id:int}')
    async def get_event(self, event_id: int) -> Event:
        pass

