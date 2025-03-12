from logging import getLogger

from litestar.di import Provide

from backend.src.infrastructure.repositories.event import provide_event_repo


async def provide_event_logger():
    return getLogger("src.events")


event_dependencies = {
    "repo": Provide(provide_event_repo),
    "logger": Provide(provide_event_logger)
}