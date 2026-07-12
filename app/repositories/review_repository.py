from sqlalchemy.orm import Session

from app.models.review import Review
from app.repositories.base import BaseRepository


class ReviewRepository(BaseRepository[Review]):

    def __init__(self):
        super().__init__(Review)

    def get_book_reviews(
        self,
        db: Session,
        book_id: int,
    ) -> list[Review]:

        return (
            db.query(Review)
            .filter(Review.book_id == book_id)
            .all()
        )

    def get_user_reviews(
        self,
        db: Session,
        user_id: int,
    ) -> list[Review]:

        return (
            db.query(Review)
            .filter(Review.user_id == user_id)
            .all()
        )