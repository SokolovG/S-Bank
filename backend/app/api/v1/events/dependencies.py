from logging import getLogger

from litestar.di import Provide

from backend.app.infrastructure.repositories.event import provide_event_repo


async def provide_event_logger():
    return getLogger("app.events")


event_dependencies = {
    "repo": Provide(provide_event_repo),
    "logger": Provide(provide_event_logger)
}