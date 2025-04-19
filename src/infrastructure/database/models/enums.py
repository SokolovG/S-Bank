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


class TransactionType(Enum):
    """Enum for transaction types."""

    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    TRANSFER = "transfer"
    PAYMENT = "payment"
    INTERNATIONAL_TRANSFER = "international_transfer"
    FEE = "fee"
    INTEREST = "interest"
    REFUND = "refund"


class TransactionStatus(Enum):
    """Enum for transaction status."""

    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REJECTED = "rejected"
    CANCELLED = "cancelled"
    PROCESSING = "processing"


class CardType(Enum):
    """Enum for card type."""

    VIRTUAL = "virtual"
    PHYSICAL = "physical"
    DEBIT = "debit"
    CREDIT = "credit"
