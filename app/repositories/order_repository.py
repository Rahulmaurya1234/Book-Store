from app.models.order import Order
from app.repositories.base import BaseRepository


class OrderRepository(BaseRepository[Order]):

    def __init__(self):
        super().__init__(Order)

    # def get_user_orders(
    #     self,
    #     db: Session,
    #     user_id: int,
    # ) -> list[Order]:

    #     return (
    #         db.query(Order)
    #         .filter(Order.user_id == user_id)
    #         .all()
    #     )