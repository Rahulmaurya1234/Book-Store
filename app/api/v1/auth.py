from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserResponse,
)
from app.services.user_service import UserService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

user_service = UserService()

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)

def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):

    try:

        return user_service.register_user(
            db,
            user,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post("/login")
def login(
    credentials: UserLogin,
    db: Session = Depends(get_db),
):

    try:

        return user_service.login_user(
            db,
            credentials,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=401,
            detail=str(e),
        )