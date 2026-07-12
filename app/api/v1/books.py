from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.dependencies.auth import get_current_admin
from app.models.user import User

from app.schemas.book import (
    BookCreate,
    BookUpdate,
    BookResponse,
)
from app.services.book_service import BookService


router = APIRouter(
    prefix="/books",
    tags=["Books"],
)

book_service = BookService()


@router.post(
    "/",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin),
):

    try:

        return book_service.create_book(
            db,
            book,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "/",
    response_model=list[BookResponse],
)
def get_books(
    db: Session = Depends(get_db),
):

    return book_service.get_all_books(db)


@router.get(
    "/{book_id}",
    response_model=BookResponse,
)
def get_book(
    book_id: int,
    db: Session = Depends(get_db),
):

    book = book_service.get_book(
        db,
        book_id,
    )

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found.",
        )

    return book


@router.put(
    "/{book_id}",
    response_model=BookResponse,
)
def update_book(
    book_id: int,
    book: BookUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin),
):

    try:

        return book_service.update_book(
            db,
            book_id,
            book,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.delete("/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin),
):

    try:

        return book_service.delete_book(
            db,
            book_id,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )