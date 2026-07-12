from sqlalchemy.orm import Session

from app.models.order_item import OrderItem
from app.repositories.base import BaseRepository


class OrderItemRepository(BaseRepository[OrderItem]):

    def __init__(self):
        super().__init__(OrderItem)

    # def get_order_items(
    #     self,
    #     db: Session,
    #     order_id: int,
    # ) -> list[OrderItem]:

    #     return (
    #         db.query(OrderItem)
    #         .filter(OrderItem.order_id == order_id)
    #         .all()
    #     )