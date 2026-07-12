from fastapi import FastAPI
from app.core.exception_handler import register_exception_handlers

from app.api.v1 import (
    auth_router,
    user_router,
    author_router,
    category_router,
    book_router,
    cart_router,
    order_router,
)

app = FastAPI(
    title="Book Store API",
    version="0.1.0",
)
register_exception_handlers(app)


from app.api.v1 import upload

app.include_router(upload.router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(author_router)
app.include_router(category_router)
app.include_router(book_router)
app.include_router(cart_router)
app.include_router(order_router)


@app.get("/")
def health():
    return {
        "message": "Book Store API Running"
    }