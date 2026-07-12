from pydantic import BaseModel, ConfigDict


class BookCreate(BaseModel):
    title: str
    description: str | None = None
    price: float
    stock: int
    language: str
    published_date: str | None = None
    cover_image: str | None = None
    author_id: int
    category_id: int


class BookUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    price: float | None = None
    stock: int | None = None
    language: str | None = None
    published_date: str | None = None
    cover_image: str | None = None
    author_id: int | None = None
    category_id: int | None = None


class BookResponse(BaseModel):
    id: int
    title: str
    description: str | None
    price: float
    stock: int
    language: str
    published_date: str | None
    cover_image: str | None
    author_id: int
    category_id: int

    model_config = ConfigDict(from_attributes=True)