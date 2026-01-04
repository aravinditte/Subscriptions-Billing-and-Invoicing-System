from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db_session
from app.domain.payments.schemas import PaymentRead
from app.services.payment_service import PaymentService

router = APIRouter()


@router.post("/{invoice_id}", response_model=PaymentRead)
def pay_invoice(
    invoice_id: int,
    db: Session = Depends(get_db_session),
):
    service = PaymentService(db)

    try:
        payment = service.charge_invoice(
            invoice_id=invoice_id,
            amount=0,  # actual amount is derived from invoice internally
        )
        return payment
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
