from enum import Enum


class CardType(Enum):
    """Enum for card type."""

    VIRTUAL = "virtual"
    PHYSICAL = "physical"
    DEBIT = "debit"
    CREDIT = "credit"
