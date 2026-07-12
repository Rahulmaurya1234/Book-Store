from sqlalchemy.orm import Session

from app.models.cart import Cart
from app.repositories.base import BaseRepository


class CartRepository(BaseRepository[Cart]):

    def __init__(self):
        super().__init__(Cart)

    def get_user_cart(
        self,
        db: Session,
        user_id: int,
    ) -> Cart | None:

        return (
            db.query(Cart)
            .filter(Cart.user_id == user_id)
            .first()
        )

    def create_cart(
        self,
        db: Session,
        user_id: int,
    ) -> Cart:

        cart = Cart(
            user_id=user_id,
        )

        return self.create(
            db,
            cart,
        )