from litestar.di import Provide
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.domain.repositories.event import EventRepository


async def provide_repositories(db_session: AsyncSession) -> dict:
    dependencies = {'event_repo': EventRepository(session=db_session)}
    return dependencies


dependencies = {
    'repositories': Provide(provide_repositories)
}
