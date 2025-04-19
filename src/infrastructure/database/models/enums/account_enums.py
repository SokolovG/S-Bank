from enum import Enum


class AccountType(str, Enum):
    """Enum for account types."""

    CURRENT = "current"
    SAVINGS = "savings"
    BUSINESS = "business"


class Currency(Enum):
    """Enum for currency types."""

    USD = "USD"
    EUR = "EUR"
    RUB = "RUB"
