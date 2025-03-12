from backend.app.api.v1.events.controllers import EventController
from litestar import Router

event_router = Router(
    path="/interfaces/api",
    route_handlers=[EventController]
)
