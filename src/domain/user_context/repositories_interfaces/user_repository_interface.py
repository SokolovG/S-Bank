from typing import Protocol

from src.domain.user_context.entities.user import UserEntity


class UserRepositoryInterface(Protocol):
    """Repository interface for User model operations."""

    async def get_by_email(self, email: str) -> UserEntity | None:
        """Get a user by email address."""

    async def save(self, user_entity: UserEntity) -> UserEntity:
        """Get a user by phone number."""
