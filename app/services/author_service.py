from sqlalchemy.orm import Session

from app.models.author import Author
from app.repositories.author_repository import AuthorRepository
from app.schemas.author import (
    AuthorCreate,
    AuthorUpdate,
)


class AuthorService:

    def __init__(self):
        self.author_repository = AuthorRepository()

    def create_author(
        self,
        db: Session,
        author_data: AuthorCreate,
    ):

        author = Author(
            name=author_data.name,
            bio=author_data.bio,
        )

        return self.author_repository.create(
            db,
            author,
        )

    def get_author(
        self,
        db: Session,
        author_id: int,
    ):

        return self.author_repository.get_by_id(
            db,
            author_id,
        )

    def get_all_authors(
        self,
        db: Session,
    ):

        return self.author_repository.get_all(db)

    def update_author(
        self,
        db: Session,
        author_id: int,
        author_data: AuthorUpdate,
    ):

        author = self.author_repository.get_by_id(
            db,
            author_id,
        )

        if not author:
            raise ValueError("Author not found.")

        if author_data.name is not None:
            author.name = author_data.name

        if author_data.bio is not None:
            author.bio = author_data.bio

        return self.author_repository.update(
            db,
            author,
        )

    def delete_author(
        self,
        db: Session,
        author_id: int,
    ):

        author = self.author_repository.get_by_id(
            db,
            author_id,
        )

        if not author:
            raise ValueError("Author not found.")

        self.author_repository.delete(
            db,
            author,
        )

        return {
            "message": "Author deleted successfully."
        }