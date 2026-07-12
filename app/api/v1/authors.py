from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.author import (
    AuthorCreate,
    AuthorUpdate,
    AuthorResponse,
)
from app.services.author_service import AuthorService

router = APIRouter(
    prefix="/authors",
    tags=["Authors"],
)

author_service = AuthorService()


@router.post(
    "/",
    response_model=AuthorResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_author(
    author: AuthorCreate,
    db: Session = Depends(get_db),
):

    return author_service.create_author(
        db,
        author,
    )

@router.get(
    "/",
    response_model=list[AuthorResponse],
)
def get_all_authors(
    db: Session = Depends(get_db),
):

    return author_service.get_all_authors(
        db,
    )

@router.get(
    "/{author_id}",
    response_model=AuthorResponse,
)
def get_author(
    author_id: int,
    db: Session = Depends(get_db),
):

    author = author_service.get_author(
        db,
        author_id,
    )

    if not author:
        raise HTTPException(
            status_code=404,
            detail="Author not found.",
        )

    return author

@router.put(
    "/{author_id}",
    response_model=AuthorResponse,
)
def update_author(
    author_id: int,
    author: AuthorUpdate,
    db: Session = Depends(get_db),
):

    try:

        return author_service.update_author(
            db,
            author_id,
            author,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

@router.delete("/{author_id}")
def delete_author(
    author_id: int,
    db: Session = Depends(get_db),
):

    try:

        return author_service.delete_author(
            db,
            author_id,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

