from enum import Enum


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
