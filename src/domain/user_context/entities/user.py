from src.common.exceptions import UserAlreadyBlockedError, UserNotBlockedError
from src.domain.user_context.events.user_events import (
    UserBlockedEvent,
    UserDeactivatedEvent,
    UserEmailChangedEvent,
    UserRegisteredEvent,
    UserUnlockedEvent,
)
from src.domain.user_context.value_objects import UserId


class UserEntity:
    """User domain model.

    This entity represents a user in the system and contains all the domain logic
    related to user account management including registration, authentication,
    blocking/unblocking, and profile changes.

    Args:
        A user cannot be both blocked and unblocked at the same time
        A blocked user is considered inactive for operational purposes
        Email must be valid and unique in the system
        Reason for blocking must be provided when blocking a user

    Attrs:
        user_id: Unique id for the user.
        email: User's email.
        hashed_password: Hashed user password.
        is_active: Indicates if account is active. Defaults to True.
        blocked: Indicates if account is blocked. Defaults to False.
        reason_for_blocking: Reason why the user was blocked, if applicable.

    """

    _events: list[object]

    user_id: UserId
    email: str
    hashed_password: str
    is_active: bool
    blocked: bool
    reason_for_blocking: str | None

    def __init__(
        self,
        user_id: UserId,
        email: str,
        hashed_password: str,
        is_active: bool = True,
        blocked: bool = False,
        reason_for_blocking: str | None = None,
    ) -> None:
        """Initialize a new UserEntity.

        Args:
            user_id: The unique id for the user.
            email: The user's email address.
            hashed_password: The hashed password for the user.
            is_active: Indicates if account is active. Defaults to True.
            blocked: Indicates if account is blocked. Defaults to False.
            reason_for_blocking: Message for reason blocking.

        """
        self._events = []
        self.user_id = user_id
        self.email = email
        self.hashed_password = hashed_password
        self.is_active = is_active
        self.blocked = blocked
        self.reason_for_blocking = reason_for_blocking

    @classmethod
    def create(cls, email: str, hashed_password: str) -> "UserEntity":
        """Create a new user with a generated UserId and active status.

        Args:
            email: The user's email address.
            hashed_password: The hashed password.

        Returns:
            UserEntity: A new instance of UserEntity.

        """
        user_id = UserId.create_new()
        user = cls(
            user_id=user_id,
            email=email,
            hashed_password=hashed_password,
            is_active=True,
        )

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
        return self.hashed_password == hashed_password

    def block(self, reason: str) -> None:
        """F."""
        if self.blocked:
            raise UserAlreadyBlockedError("User is already blocked")
        self.blocked = True
        self.reason_for_blocking = reason

        event = UserBlockedEvent(user_id=self.user_id, email=self.email, reason=self.reason_for_blocking)
        self._events.append(event)

    def unlock(self) -> None:
        """F."""
        if not self.blocked:
            raise UserNotBlockedError("User is not blocked")

        self.blocked = False
        if self.reason_for_blocking:
            self.reason_for_blocking = ""

        event = UserUnlockedEvent(user_id=self.user_id, email=self.email)
        self._events.append(event)

    def deactivate(self) -> None:
        """Deactivate the user account.

        Deactivation is typically used for accounts that are no longer
        in use but should be preserved for record-keeping.
        """
        if not self.is_active:
            return  # Already deactivated, no action needed

        self.is_active = False

        event = UserDeactivatedEvent(user_id=self.user_id, email=str(self.email))
        self._events.append(event)

    def activate(self) -> None:
        """Activate a deactivated user account.

        Reactivates an account that was previously deactivated.
        Note that this doesn't unblock a blocked account.

        Raises:
            UserBlockedError: If the user is currently blocked.

        """
        if self.blocked:
            raise UserAlreadyBlockedError(self.email)

        # If already active, do nothing
        if self.is_active:
            return

        self.is_active = True

    def is_operational(self) -> bool:
        """Check if the user account is operational.

        An operational account is both active and not blocked.

        Returns:
            bool: True if the user can perform operations, False otherwise.

        """
        return self.is_active and not self.blocked

    def change_email(self, new_email: str) -> None:
        """Update the user's email address.

        Args:
            new_email: The new email address for the user.

        """
        if self.email == new_email:
            return

        old_email = self.email
        self.email = new_email

        event = UserEmailChangedEvent(user_id=self.user_id, old_email=old_email, new_email=new_email)
        self._events.append(event)

    def get_events(self) -> list[object]:
        """Get all accumulated events.

        Returns:
            list of events.

        """
        return self._events.copy()

    def clear_events(self) -> None:
        """Clear the list of events."""
        self._events.clear()
