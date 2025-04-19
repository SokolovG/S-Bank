from typing import Any, ClassVar, TypeVar

T = TypeVar("T")


class BaseCommonError(Exception):
    """Base class for custom domain exceptions.

    Used to create specific error types with a value, code, message, and optional details.

    Attributes:
        context: The error's context

    """

    context: ClassVar[str]

    def __init__(self, value: T, code: str, msg: str, details: dict[str, Any] | None = None) -> None:
        """Initialize the error with a value, code, message, and optional details.

        Args:
            value: The value causing the error.
            code: A unique error code.
            msg: A description of the error.
            details: Additional error info. Defaults to None.

        """
        self.value = value
        self.error_code = code
        self.msg = msg
        self.detail = details
