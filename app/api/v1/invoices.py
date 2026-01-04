from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db_session
from app.domain.invoices.schemas import InvoiceRead
from app.domain.invoices.repository import InvoiceRepository

router = APIRouter()


@router.get("/{invoice_id}", response_model=InvoiceRead)
def get_invoice(
    invoice_id: int,
    db: Session = Depends(get_db_session),
):
    repo = InvoiceRepository(db)
    invoice = repo.get(invoice_id)

    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    return invoice
