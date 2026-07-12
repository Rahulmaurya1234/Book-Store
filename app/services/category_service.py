from sqlalchemy.orm import Session

from app.models.category import Category
from app.repositories.category_repository import CategoryRepository
from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
)


class CategoryService:

    def __init__(self):
        self.category_repository = CategoryRepository()

    def create_category(
        self,
        db: Session,
        category_data: CategoryCreate,
    ):

        existing = self.category_repository.get_by_name(
            db,
            category_data.name,
        )

        if existing:
            raise ValueError("Category already exists.")

        category = Category(
            name=category_data.name,
            description=category_data.description,
        )

        return self.category_repository.create(
            db,
            category,
        )

    def get_category(
        self,
        db: Session,
        category_id: int,
    ):
        return self.category_repository.get_by_id(
            db,
            category_id,
        )

    def get_all_categories(
        self,
        db: Session,
    ):
        return self.category_repository.get_all(db)

    def update_category(
        self,
        db: Session,
        category_id: int,
        category_data: CategoryUpdate,
    ):

        category = self.category_repository.get_by_id(
            db,
            category_id,
        )

        if not category:
            raise ValueError("Category not found.")

        if category_data.name is not None:
            category.name = category_data.name

        if category_data.description is not None:
            category.description = category_data.description

        return self.category_repository.update(
            db,
            category,
        )

    def delete_category(
        self,
        db: Session,
        category_id: int,
    ):

        category = self.category_repository.get_by_id(
            db,
            category_id,
        )

        if not category:
            raise ValueError("Category not found.")

        self.category_repository.delete(
            db,
            category,
        )

        return {
            "message": "Category deleted successfully."
        }