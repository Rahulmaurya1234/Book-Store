from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.order import OrderResponse
from app.services.order_service import OrderService
from app.dependencies.auth import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)

order_service = OrderService()

USER_ID = 1


@router.post("/checkout")
def checkout(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return order_service.checkout(
        db,
        current_user.id,
    )