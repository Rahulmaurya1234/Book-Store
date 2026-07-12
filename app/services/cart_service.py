from sqlalchemy.orm import Session

from app.models.cart_item import CartItem

from app.repositories.book_repository import BookRepository
from app.repositories.cart_item_repository import CartItemRepository
from app.repositories.cart_repository import CartRepository

from app.schemas.cart_item import (
    CartItemCreate,
    CartItemUpdate,
)


class CartService:

    def __init__(self):

        self.cart_repository = CartRepository()

        self.cart_item_repository = CartItemRepository()

        self.book_repository = BookRepository()




    def get_cart(
        self,
        db: Session,
        user_id: int,
        ):

        cart = self.cart_repository.get_user_cart(
            db,
            user_id,
        )

        if not cart:
            cart = self.cart_repository.create_cart(
                db,
                user_id,
            )

        return cart

    def add_book(
        self,
        db: Session,
        user_id: int,
        item: CartItemCreate,
    ):

        cart = self.cart_repository.get_user_cart(
            db,
            user_id,
        )

        if not cart:
            cart = self.cart_repository.create_cart(
                db,
                user_id,
            )

        book = self.book_repository.get_by_id(
            db,
            item.book_id,
        )

        if not book:
            raise ValueError("Book not found.")

        cart_item = self.cart_item_repository.get_cart_item(
            db,
            cart.id,
            item.book_id,
        )

        if cart_item:

            cart_item.quantity += item.quantity

            return self.cart_item_repository.update(
                db,
                cart_item,
            )

        cart_item = CartItem(
            cart_id=cart.id,
            book_id=item.book_id,
            quantity=item.quantity,
        )

        return self.cart_item_repository.create(
            db,
            cart_item,
        )

    def update_quantity(
            self,
            db: Session,
            user_id: int,
            item_id: int,
            data: CartItemUpdate,
        ):

        cart = self.cart_repository.get_user_cart(
            db,
            user_id,
        )

        if not cart:
            raise ValueError("Cart not found.")

        item = self.cart_item_repository.get_cart_item_by_id(
            db,
            cart.id,
            item_id,
        )

        if not item:
            raise ValueError("Cart item not found.")

        item.quantity = data.quantity

        return self.cart_item_repository.update(
            db,
            item,
        )

    def remove_item(
            self,
            db: Session,
            user_id: int,
            item_id: int,
        ):

            cart = self.cart_repository.get_user_cart(
                db,
                user_id,
            )

            if not cart:
                raise ValueError("Cart not found.")

            item = self.cart_item_repository.get_cart_item_by_id(
                db,
                cart.id,
                item_id,
            )

            if not item:
                raise ValueError("Cart item not found.")

            self.cart_item_repository.delete(
                db,
                item,
            )

            return {
                "message": "Item removed successfully."
            }




    def clear_cart(
        self,
        db: Session,
        user_id: int,
    ):

        cart = self.cart_repository.get_user_cart(
            db,
            user_id,
        )

        if not cart:
            raise ValueError("Cart not found.")

        items = self.cart_item_repository.get_cart_items(
            db,
            cart.id,
        )

        for item in items:
            self.cart_item_repository.delete(
                db,
                item,
            )

        return {
            "message": "Cart cleared successfully."
        }

