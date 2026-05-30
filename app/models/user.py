from datetime import datetime

from sqlalchemy import (
    BigInteger,
    Boolean,
    DateTime,
    Integer,
    String
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)


class Base(DeclarativeBase):
    pass


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True
    )

    username: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    full_name: Mapped[str] = mapped_column(
        String(255)
    )

    free_requests: Mapped[int] = mapped_column(
        Integer,
        default=3
    )

    is_premium: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    premium_until: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )