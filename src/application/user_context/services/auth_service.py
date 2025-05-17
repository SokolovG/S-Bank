from src.common.event_bus import EventBus
from src.common.exceptions.user_exceptions import (
    UserExistError,
    UserIsNotActiveError,
    UserNotFoundError,
    UserNoVerifyPasswordError,
)
from src.domain.user_context.entities.user import UserEntity
from src.domain.user_context.repositories_interfaces.user_repository_interface import (
    IUserRepository,
)


class AuthService:
    """Service for handling user authentication and registration.

    Provides methods to authenticate and register users, interacting with the user repository.

    Attributes:
        user_repository: Repository for user data operations.
        secret_key: Secret key used for authentication processes.

    """

    def __init__(self, user_repository: IUserRepository, secret_key: str, event_bus: EventBus) -> None:
        """Initialize the AuthService.

        Args:
            user_repository: The repository to handle user data.
            secret_key: The secret key for authentication.
            event_bus: The Event bus for user events.

        """
        self.user_repository = user_repository
        self.secret_key = secret_key
        self._event_bus = event_bus

    async def authenticate_user(self, email: str, password: str) -> UserEntity:
        """Authenticate a user by email and password.

        Args:
            email: The user's email address.
            password: The user's password.

        Returns:
            UserEntity: The authenticated user entity.

        Raises:
            UserNotFoundError: If no user is found with the provided email.
            UserIsNotActiveError: If the user account is not active.
            UserNoVerifyPasswordError: If the password does not match.

        """
        user = await self.user_repository.get_by_email(email)

        if not user:
            raise UserNotFoundError(email)

        if not user.is_active:
            raise UserIsNotActiveError(email)

        if not user.verify_password(password):
            raise UserNoVerifyPasswordError(password)

        return user

    async def register_user(self, email: str, hashed_password: str) -> UserEntity:
        """Register a new user with the provided email and password hash.

        Args:
            email: The user's email address.
            hashed_password: The hashed password for the user.

        Returns:
            UserEntity: The newly created and saved user entity.

        Raises:
            UserExistError: If a user with the provided email already exists.

        """
        existing_user = await self.user_repository.get_by_email(email)

        if existing_user:
            raise UserExistError(email)

        user_entity = UserEntity.create(email=email, hashed_password=hashed_password)
        saved_user = await self.user_repository.save(user_entity)

        events = user_entity.get_events()
        for event in events:
            self._event_bus.publish(event)

        user_entity.clear_events()

        return saved_user

    async def block_user(self, email: str, reason: str) -> None:
        """Block a user account.

        Args:
            email: Email of the user to block.
            reason: Reason for blocking the user.

        Returns:
            UserEntity: The blocked user entity.

        Raises:
            UserNotFoundError: If no user is found with the provided email.

        """
        user_entity = await self.user_repository.get_by_email(email)
        if not user_entity:
            raise UserNotFoundError(f"User with ID {email} not found")

        user_entity.block(reason)
        await self.user_repository.save(user_entity)

        events = user_entity.get_events()
        for event in events:
            self._event_bus.publish(event)

        user_entity.clear_events()

    async def unlock_user(self, email: str) -> UserEntity:
        """Unblock a user account.

        Args:
            email: Email of the user to unblock.

        Returns:
            UserEntity: The unblocked user entity.

        Raises:
            UserNotFoundError: If no user is found with the provided email.

        """
        user_entity = await self.user_repository.get_by_email(email)
        if not user_entity:
            raise UserNotFoundError(f"User with email {email} not found")

        user_entity.unlock()

        saved_user = await self.user_repository.save(user_entity)

        # Публикация событий
        events = user_entity.get_events()
        for event in events:
            self._event_bus.publish(event)

        user_entity.clear_events()

        return saved_user

    async def change_email(self, old_email: str, new_email: str) -> UserEntity:
        """Change a user's email address.

        Args:
            old_email: Current email of the user.
            new_email: New email for the user.

        Returns:
            UserEntity: The updated user entity.

        Raises:
            UserNotFoundError: If no user is found with the provided email.
            UserExistError: If a user with the new email already exists.

        """
        user_entity = await self.user_repository.get_by_email(old_email)
        if not user_entity:
            raise UserNotFoundError(f"User with email {old_email} not found")

        existing_user = await self.user_repository.get_by_email(new_email)
        if existing_user:
            raise UserExistError(f"User with email {new_email} already exists")

        user_entity.change_email(new_email)

        saved_user = await self.user_repository.save(user_entity)

        events = user_entity.get_events()
        for event in events:
            self._event_bus.publish(event)

        user_entity.clear_events()

        return saved_user
