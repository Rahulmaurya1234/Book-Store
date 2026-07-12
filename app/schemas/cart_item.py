from pydantic import BaseModel, ConfigDict


class CartItemCreate(BaseModel):
    book_id: int
    quantity: int


class CartItemUpdate(BaseModel):
    quantity: int


class CartItemResponse(BaseModel):
    id: int
    quantity: int
    cart_id: int
    book_id: int

    model_config = ConfigDict(
        from_attributes=True
    )