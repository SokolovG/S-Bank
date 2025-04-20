from src.domain.user_context.events.user_events import UserRegisteredEvent
from src.domain.user_context.value_objects import UserId


class UserEntity:
    """User domain model.

    Attributes:
        user_id: Unique id for the user.
        email: User's email.
        password_hash: Hashed user password.
        is_active: Indicates if account is active. Defaults to True.

    """

    _events: list[object]

    user_id: UserId
    email: str
    password_hash: str
    is_active: bool = True

    def __init__(self, user_id: UserId, email: str, password_hash: str, is_active: bool = True) -> None:
        """Initialize a new UserEntity.

        Args:
            user_id: The unique id for the user.
            email: The user's email address.
            password_hash: The hashed password for the user.
            is_active: Indicates if account is active. Defaults to True.

        """
        self._events = []
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash
        self.is_active = is_active

    @classmethod
    def create(cls, email: str, password_hash: str) -> "UserEntity":
        """Create a new user with a generated UserId and active status.

        Args:
            email: The user's email address.
            password_hash: The hashed password.

        Returns:
            UserEntity: A new instance of UserEntity.

        """
        user_id = UserId.create_new()
        user = cls(user_id=user_id, email=email, password_hash=password_hash, is_active=True)

        event = UserRegisteredEvent(user_id=user_id, email=email)
        user._events.append(event)

        return user

    def verify_password(self, hashed_password: str) -> bool:
        """Check if the provided hashed password matches the user's password.

        Args:
            hashed_password: The hashed password to verify.

        Returns:
            bool: True if the password matches, False otherwise.

        """
        return self.password_hash == hashed_password

    def deactivate(self) -> None:
        """Deactivate the user account.

        Sets the is_active attribute to False.

        """
        self.is_active = False

    def change_email(self, new_email: str) -> None:
        """Update the user's email address.

        Args:
            new_email: The new email address for the user.

        """
        self.email = new_email

    def get_events(self) -> list[object]:
        """Get all accumulated events.

        Returns:
            list of events.

        """
        return self._events.copy()

    def clear_events(self) -> None:
        """Clear the list of events."""
        self._events.clear()
