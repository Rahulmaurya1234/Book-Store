from pydantic import BaseModel, ConfigDict


class ReviewCreate(BaseModel):
    rating: int
    comment: str | None = None
    user_id: int
    book_id: int


class ReviewUpdate(BaseModel):
    rating: int | None = None
    comment: str | None = None


class ReviewResponse(BaseModel):
    id: int
    rating: int
    comment: str | None
    user_id: int
    book_id: int

    model_config = ConfigDict(from_attributes=True)