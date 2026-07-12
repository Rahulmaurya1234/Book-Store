from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app.models.book import Book
from app.repositories.base import BaseRepository


class BookRepository(BaseRepository[Book]):

    def __init__(self):
        super().__init__(Book)

    def get_by_title(
        self,
        db: Session,
        title: str,
    ) -> Book | None:

        return (
            db.query(Book)
            .filter(Book.title == title)
            .first()
        )

    def get_by_author(
        self,
        db: Session,
        author_id: int,
    ) -> list[Book]:

        return (
            db.query(Book)
            .filter(Book.author_id == author_id)
            .all()
        )

    def get_by_category(
        self,
        db: Session,
        category_id: int,
    ) -> list[Book]:

        return (
            db.query(Book)
            .filter(Book.category_id == category_id)
            .all()
        )

    def get_books(
        self,
        db: Session,
        page: int = 1,
        size: int = 10,
        search: str | None = None,
        author_id: int | None = None,
        category_id: int | None = None,
        sort: str | None = None,
    ):

        query = db.query(Book)

        # Search
        if search:
            query = query.filter(
                Book.title.ilike(f"%{search}%")
            )

        # Filter by Author
        if author_id:
            query = query.filter(
                Book.author_id == author_id
            )

        # Filter by Category
        if category_id:
            query = query.filter(
                Book.category_id == category_id
            )

        # Sorting
        if sort:

            if sort == "price":
                query = query.order_by(
                    asc(Book.price)
                )

            elif sort == "-price":
                query = query.order_by(
                    desc(Book.price)
                )

            elif sort == "title":
                query = query.order_by(
                    asc(Book.title)
                )

            elif sort == "-title":
                query = query.order_by(
                    desc(Book.title)
                )

        total = query.count()

        books = (
            query.offset((page - 1) * size)
            .limit(size)
            .all()
        )

        return {
            "total": total,
            "page": page,
            "size": size,
            "items": books,
        }