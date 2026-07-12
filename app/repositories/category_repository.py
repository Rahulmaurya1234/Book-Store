from sqlalchemy.orm import Session

from app.models.category import Category
from app.repositories.base import BaseRepository


class CategoryRepository(BaseRepository[Category]):

    def __init__(self):
        super().__init__(Category)

    def get_by_name(
        self,
        db: Session,
        name: str,
    ) -> Category | None:

        return (
            db.query(Category)
            .filter(Category.name == name)
            .first()
        )