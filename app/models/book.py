from sqlalchemy import String, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(1000)
    )

    price: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    stock: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    language: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    published_date: Mapped[str | None] = mapped_column(
        String(20)
    )

    cover_image: Mapped[str | None] = mapped_column(
        String(255)
    )

    author_id: Mapped[int] = mapped_column(
        ForeignKey("authors.id"),
        nullable=False,
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False,
    )

    author: Mapped["Author"] = relationship(
        back_populates="books"
    )

    category: Mapped["Category"] = relationship(
        back_populates="books"
    )

    reviews: Mapped[list["Review"]] = relationship(
        back_populates="book"
    )

    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="book"
    )

    cart_items = relationship(
        "CartItem",
        back_populates="book",
    )