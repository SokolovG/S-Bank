from sqlalchemy.ext.asyncio import AsyncSession


class UserStatisticsRepository:
    def __init__(self, session: AsyncSession) -> None:
        """F."""
        self.session = session
