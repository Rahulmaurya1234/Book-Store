from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Cart(Base):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        unique=True,
    )

    user = relationship(
        "User",
        back_populates="cart",
    )

    cart_items = relationship(
        "CartItem",
        back_populates="cart",
        cascade="all, delete-orphan",
    )