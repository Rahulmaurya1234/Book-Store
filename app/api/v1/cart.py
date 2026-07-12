from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.cart import CartResponse
from app.schemas.cart_item import (
    CartItemCreate,
    CartItemUpdate,
    CartItemResponse,
)

from app.services.cart_service import CartService


router = APIRouter(
    prefix="/cart",
    tags=["Cart"],
)

cart_service = CartService()


@router.get(
    "/",
    response_model=CartResponse,
)
def get_cart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    cart = cart_service.get_cart(
        db,
        current_user.id,
    )

    if not cart:
        raise HTTPException(
            status_code=404,
            detail="Cart not found.",
        )

    return cart


@router.post(
    "/add",
    response_model=CartItemResponse,
)
def add_book(
    item: CartItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    try:
        return cart_service.add_book(
            db,
            current_user.id,
            item,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.put(
    "/item/{item_id}",
    response_model=CartItemResponse,
)
def update_quantity(
    item_id: int,
    item: CartItemUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),  # authentication required
):

    try:
        return cart_service.update_quantity(
            db,
            current_user.id,
            item_id,
            item,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.delete("/item/{item_id}")
def remove_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    try:

        return cart_service.remove_item(
            db,
            current_user.id,
            item_id,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )
        
@router.delete("/clear")
def clear_cart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    try:
        return cart_service.clear_cart(
            db,
            current_user.id,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )