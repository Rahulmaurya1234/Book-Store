from pydantic import BaseModel, ConfigDict


class CartResponse(BaseModel):
    id: int
    user_id: int

    model_config = ConfigDict(
        from_attributes=True
    )