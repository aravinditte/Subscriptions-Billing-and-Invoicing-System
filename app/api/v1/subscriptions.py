from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db_session
from app.domain.subscriptions.schemas import (
    SubscriptionCreate,
    SubscriptionRead,
)
from app.services.subscription_service import SubscriptionService

router = APIRouter()


@router.post("/", response_model=SubscriptionRead)
def create_subscription(
    payload: SubscriptionCreate,
    db: Session = Depends(get_db_session),
):
    service = SubscriptionService(db)

    return service.create_subscription(
        user_id=payload.user_id,
        plan_id=payload.plan_id,
        start_date=payload.start_date,
        next_billing_date=payload.next_billing_date,
    )


@router.post("/{subscription_id}/cancel", response_model=SubscriptionRead)
def cancel_subscription(
    subscription_id: int,
    db: Session = Depends(get_db_session),
):
    service = SubscriptionService(db)

    try:
        return service.update_status(subscription_id, "cancelled")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
