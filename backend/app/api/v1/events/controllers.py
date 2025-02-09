"""Module for event controller.

Contains the following routes:
    - GET /events
"""
from __future__ import annotations

from litestar import get, Controller

from backend.app.domain.schemas.events.event import EventRead


class EventController(Controller):
    """Basic event controller.

    Contains dependencies with EventRepository
    """

    path = '/events'

    @get()
    async def get_events(self, repositories: dict) -> list[EventRead]:
        event_repo = repositories.get('event_repo')
        events = await event_repo.list()
        return events

    @get('/{event_id:int}')
    async def get_event(self, repositories: dict, event_id: int) -> EventRead:
        event_repo = repositories.get('event_repo')
        event = await event_repo.get_one_or_none(id=event_id)
        return event
