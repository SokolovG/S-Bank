from litestar import Router

from backend.app.api.v1.events.controllers import EventController


event_router = Router(
    path="/api/v1",
    route_handlers=[EventController]
)