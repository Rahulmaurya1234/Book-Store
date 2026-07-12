from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    phone: Mapped[str | None] = mapped_column(
        String(20)
    )

    role: Mapped[str] = mapped_column(
        String(20),
        default="CUSTOMER",
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    orders: Mapped[list["Order"]] = relationship(
        back_populates="user"
    )

    reviews: Mapped[list["Review"]] = relationship(
        back_populates="user"
    )
    cart = relationship(
        "Cart",
        back_populates="user",
        uselist=False,
    )