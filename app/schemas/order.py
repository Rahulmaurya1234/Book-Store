from pydantic import BaseModel, ConfigDict


class OrderCreate(BaseModel):
    user_id: int


class OrderUpdate(BaseModel):
    status: str


class OrderResponse(BaseModel):
    id: int
    total_amount: float
    status: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)