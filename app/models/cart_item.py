from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    cart_id: Mapped[int] = mapped_column(
        ForeignKey("carts.id"),
        nullable=False,
    )

    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id"),
        nullable=False,
    )

    cart = relationship(
        "Cart",
        back_populates="cart_items",
    )

    book = relationship(
        "Book",
        back_populates="cart_items",
    )