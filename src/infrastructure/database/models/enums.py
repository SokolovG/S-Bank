from enum import Enum


class AccountType(str, Enum):
    CURRENT = "current"
    SAVINGS = "savings"
    BUSINESS = "business"


class Currency(str, Enum):
    """Enum for currency types.

    Attributes:
        USD: United States Dollar
        EUR: Euro
        RUB: Russian Ruble

    """

    USD = "USD"
    EUR = "EUR"
    RUB = "RUB"

class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    TRANSFER = "transfer"
    PAYMENT = "payment"
    INTERNATIONAL_TRANSFER = "international_transfer"
    FEE = "fee"
    INTEREST = "interest"
    REFUND = "refund"


class TransactionStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REJECTED = "rejected"
    CANCELLED = "cancelled"
    PROCESSING = "processing"


class CardType(str, Enum):
    VIRTUAL = "virtual"
    PHYSICAL = "physical"
    DEBIT = "debit"
    CREDIT = "credit"
