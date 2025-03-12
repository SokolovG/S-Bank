from litestar import Router

from backend.src.interfaces.api.controllers.controllers import EventController

event_router = Router(
    path="/api/v1",
    route_handlers=[EventController]
)
