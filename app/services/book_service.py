from sqlalchemy.orm import Session

from app.models.book import Book
from app.repositories.author_repository import AuthorRepository
from app.repositories.book_repository import BookRepository
from app.repositories.category_repository import CategoryRepository

from app.schemas.book import BookCreate, BookUpdate


class BookService:

    def __init__(self):
        self.book_repository = BookRepository()
        self.author_repository = AuthorRepository()
        self.category_repository = CategoryRepository()

    def create_book(
        self,
        db: Session,
        book_data: BookCreate,
    ):

        existing = self.book_repository.get_by_title(
            db,
            book_data.title,
        )

        if existing:
            raise ValueError("Book already exists.")

        author = self.author_repository.get_by_id(
            db,
            book_data.author_id,
        )

        if not author:
            raise ValueError("Author not found.")

        category = self.category_repository.get_by_id(
            db,
            book_data.category_id,
        )

        if not category:
            raise ValueError("Category not found.")

        if book_data.price <= 0:
            raise ValueError("Price must be greater than zero.")

        if book_data.stock < 0:
            raise ValueError("Stock cannot be negative.")

        book = Book(
            title=book_data.title,
            description=book_data.description,
            price=book_data.price,
            stock=book_data.stock,
            language=book_data.language,
            published_date=book_data.published_date,
            cover_image=book_data.cover_image,
            author_id=book_data.author_id,
            category_id=book_data.category_id,
        )

        return self.book_repository.create(
            db,
            book,
        )

    def get_book(
        self,
        db: Session,
        book_id: int,
    ):
        return self.book_repository.get_by_id(
            db,
            book_id,
        )

    def get_all_books(
        self,
        db: Session,
    ):
        return self.book_repository.get_all(db)

    def update_book(
        self,
        db: Session,
        book_id: int,
        book_data: BookUpdate,
    ):

        book = self.book_repository.get_by_id(
            db,
            book_id,
        )

        if not book:
            raise ValueError("Book not found.")

        update_data = book_data.model_dump(
            exclude_unset=True,
            exclude_none=True,
        )

        for key, value in update_data.items():
            setattr(book, key, value)

        return self.book_repository.update(
            db,
            book,
        )

    def delete_book(
        self,
        db: Session,
        book_id: int,
    ):

        book = self.book_repository.get_by_id(
            db,
            book_id,
        )

        if not book:
            raise ValueError("Book not found.")

        self.book_repository.delete(
            db,
            book,
        )

        return {
            "message": "Book deleted successfully."
        }