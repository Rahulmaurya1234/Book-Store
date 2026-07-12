from app.models.author import Author
from app.repositories.base import BaseRepository


class AuthorRepository(BaseRepository[Author]):

    def __init__(self):
        super().__init__(Author)