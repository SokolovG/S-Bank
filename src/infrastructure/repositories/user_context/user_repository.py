from pydantic import EmailStr
from sqlalchemy import select

from src.infrastructure.database.models import User
from src.infrastructure.repositories.base import BasicRepository


class UserRepository(BasicRepository[User]):
    """Repository for the User model.

    Contains some custom functions.
    """

    model_type: type[User] = User

    async def get_by_username(self, username: str) -> User | None:
        """Get user by username.

        Args:
            username: Customer username

        """
        statement = select(User).where(User.username == username)
        user: User = await self.session.scalar(statement)
        return user

    async def get_by_email(self, email: EmailStr) -> User | None:
        """Get user by email.

        Args:
            email: Customer email

        """
        statement = select(User).where(User.email == email)
        user: User = await self.session.scalar(statement)
        return user

    async def get_by_phone(self, phone: str) -> User | None:
        """Get user by phone.

        Args:
            phone: Customer phone

        """
        statement = select(User).where(User.phone == phone)
        user: User = await self.session.scalar(statement)
        return user
