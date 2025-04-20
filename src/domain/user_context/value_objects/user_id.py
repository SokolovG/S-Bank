import uuid
from dataclasses import dataclass


@dataclass
class UserId:
    """A value object representing a unique user id.

    Attributes:
        value: The UUID value of the user id.

    """

    value: uuid.UUID

    @classmethod
    def create_new(cls) -> "UserId":
        """Create a new UserId with a randomly generated UUID.

        Returns:
            UserId: A new UserId instance with a unique UUID.

        """
        return cls(uuid.uuid4())

    @classmethod
    def from_string(cls, id_string: str) -> "UserId":
        """Create a UserId from a UUID string.

        Args:
            id_string: A string representation of a UUID.

        Returns:
            UserId: A UserId instance with the parsed UUID.

        """
        return cls(uuid.UUID(id_string))

    def __str__(self) -> str:
        """Return the string representation of the UserId.

        Returns:
            str: The string representation of the UUID value.

        """
        return str(self.value)
