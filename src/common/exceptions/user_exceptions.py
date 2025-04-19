from typing import Any, TypeVar

from src.common.exceptions.base_exception import BaseCommonError

T = TypeVar("T")


class UserError(BaseCommonError):
    """Base class for user-related errors.

    Extends BaseCommonError to handle errors specific to user operations.

    Attributes:
        context: The error category, set to "user".

    """

    context = "user"

    def __init__(self, value: T, code: str, msg: str, details: dict[str, Any] | None = None) -> None:
        """Initialize the user error with a value, code, message, and optional details.

        Args:
            value: The value causing the error.
            code: A unique error code, prefixed with the context.
            msg: A description of the error.
            details: Extra error info. Defaults to None.

        """
        code = f"{self.context}.{code}"
        super().__init__(value, code, msg, details)


class UserNotFoundError(UserError):
    """Error raised when a user is not found."""

    def __init__(self, identifier: T) -> None:
        """Initialize the error with the user identifier.

        Args:
            identifier: The identifier of the user that was not found.

        """
        super().__init__(
            value=identifier,
            code="not_found",
            msg="User not found",
        )


class UserIsNotActiveError(UserError):
    """Error raised when a user is not active."""

    def __init__(self, identifier: T) -> None:
        """Initialize the error with the user identifier.

        Args:
            identifier: The identifier of the inactive user.

        """
        super().__init__(
            value=identifier,
            code="not_active",
            msg="User is not active",
        )


class UserNoVerifyPasswordError(UserError):
    """Error raised when a user's password does not match."""

    def __init__(self, identifier: T) -> None:
        """Initialize the error with the user identifier.

        Args:
            identifier: The identifier of the user with the invalid password.

        """
        super().__init__(
            value=identifier,
            code="not_verify",
            msg="User password is not matching",
        )


class UserExistError(UserError):
    """Error raised when a user already exists."""

    def __init__(self, identifier: T) -> None:
        """Initialize the error with the user identifier.

        Args:
            identifier: The identifier of the user that already exists.

        """
        super().__init__(
            value=identifier,
            code="user_exist",
            msg=f"User with {identifier} exist",
        )
