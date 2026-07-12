from pydantic import BaseModel, ConfigDict


class OrderItemCreate(BaseModel):
    quantity: int
    price: float
    order_id: int
    book_id: int


class OrderItemUpdate(BaseModel):
    quantity: int | None = None
    price: float | None = None


class OrderItemResponse(BaseModel):
    id: int
    quantity: int
    price: float
    order_id: int
    book_id: int

    model_config = ConfigDict(from_attributes=True)