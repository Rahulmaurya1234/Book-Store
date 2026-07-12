from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.order_item import OrderItem

from app.repositories.order_repository import OrderRepository
from app.repositories.order_item_repository import OrderItemRepository
from app.repositories.cart_repository import CartRepository
from app.repositories.cart_item_repository import CartItemRepository
from app.repositories.book_repository import BookRepository


class OrderService:

    def __init__(self):

        self.order_repository = OrderRepository()
        self.order_item_repository = OrderItemRepository()
        self.cart_repository = CartRepository()
        self.cart_item_repository = CartItemRepository()
        self.book_repository = BookRepository()

    def checkout(
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

        cart_items = self.cart_item_repository.get_cart_items(
            db,
            cart.id,
        )

        if not cart_items:
            raise ValueError("Cart is empty.")

        total = 0

        for item in cart_items:

            book = self.book_repository.get_by_id(
                db,
                item.book_id,
            )

            if not book:
                raise ValueError("Book not found.")

            if book.stock < item.quantity:
                raise ValueError(
                    f"{book.title} is out of stock."
                )

            total += book.price * item.quantity

        order = Order(
            total_amount=total,
            status="PLACED",
            user_id=user_id,
        )

        order = self.order_repository.create(
            db,
            order,
        )

        for item in cart_items:

            book = self.book_repository.get_by_id(
                db,
                item.book_id,
            )

            order_item = OrderItem(
                order_id=order.id,
                book_id=book.id,
                quantity=item.quantity,
                price=book.price,
            )

            self.order_item_repository.create(
                db,
                order_item,
            )

            book.stock -= item.quantity

            self.book_repository.update(
                db,
                book,
            )

            self.cart_item_repository.delete(
                db,
                item,
            )

        return order