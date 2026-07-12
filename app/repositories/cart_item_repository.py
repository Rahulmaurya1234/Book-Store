from sqlalchemy.orm import Session

from app.models.cart_item import CartItem
from app.repositories.base import BaseRepository


class CartItemRepository(BaseRepository[CartItem]):

    def __init__(self):
        super().__init__(CartItem)

    def get_cart_items(
        self,
        db: Session,
        cart_id: int,
    ) -> list[CartItem]:

        return (
            db.query(CartItem)
            .filter(CartItem.cart_id == cart_id)
            .all()
        )

    def get_cart_item(
        self,
        db: Session,
        cart_id: int,
        book_id: int,
    ) -> CartItem | None:

        return (
            db.query(CartItem)
            .filter(
                CartItem.cart_id == cart_id,
                CartItem.book_id == book_id,
            )
            .first()
        )

    def get_cart_item_by_id(
        self,
        db: Session,
        cart_id: int,
        item_id: int,
    ) -> CartItem | None:

        return (
            db.query(CartItem)
            .filter(
                CartItem.id == item_id,
                CartItem.cart_id == cart_id,
            )
            .first()
        )