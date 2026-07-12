from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.repositories.user_repository import UserRepository
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)


class UserService:

    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(
        self,
        db: Session,
        user_data: UserCreate,
    ):

        existing_user = self.user_repository.get_by_email(
            db,
            user_data.email,
        )

        if existing_user:
            raise ValueError(
                "Email already registered."
            )

        hashed_password = hash_password(
            user_data.password
        )

        user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            password_hash=hashed_password,
            phone=user_data.phone,
        )

        return self.user_repository.create(
            db,
            user,
        )

    def login_user(
        self,
        db: Session,
        credentials: UserLogin,
    ):

        user = self.user_repository.get_by_email(
            db,
            credentials.email,
        )

        if not user:
            raise ValueError(
                "Invalid email or password."
            )

        if not verify_password(
            credentials.password,
            user.password_hash,
        ):
            raise ValueError(
                "Invalid email or password."
            )

        token = create_access_token(
            {
                "sub": str(user.id),
                "role": user.role,
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }