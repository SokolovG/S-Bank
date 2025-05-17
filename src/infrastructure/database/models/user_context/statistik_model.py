from decimal import Decimal

from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.base import Base


class UserStatistics(Base):
    __tablename__ = "user_statistics"
    total_users_count: Mapped[int]
    active_users_count: Mapped[int]
    verified_users_count: Mapped[int]
    blocked_users: Mapped[int]


class CustomerStatistics(Base):
    __tablename__ = "customer_statistics"
    users_by_country: Mapped[dict] = mapped_column(JSON)
    open_bill: Mapped[int]
    all_customers_balance: Mapped[Decimal]
