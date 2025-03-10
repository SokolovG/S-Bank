from logging import Logger, getLogger
from typing import TypedDict

from litestar.di import Provide
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.infrastructure.repositories.event import EventRepository


class LoggerDependencies(TypedDict):
    event_logger: Logger

class RepositoryDependencies(TypedDict):
    event_repo: EventRepository

async def provide_logger() -> LoggerDependencies:
    dependencies: LoggerDependencies = {'event_logger': getLogger('app.events')}
    return dependencies

async def provide_repositories(db_session: AsyncSession) -> RepositoryDependencies:
    dependencies: RepositoryDependencies = {
        "event_repo": EventRepository(session=db_session)
    }
    return dependencies


dependencies = {
    "repositories": Provide(provide_repositories),
    "logger": Provide(provide_logger)
}
