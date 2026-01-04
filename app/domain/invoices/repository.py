from sqlalchemy.orm import Session

from app.domain.invoices.models import Invoice


class InvoiceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, **data) -> Invoice:
        invoice = Invoice(**data)
        self.db.add(invoice)
        self.db.commit()
        self.db.refresh(invoice)
        return invoice

    def get(self, invoice_id: int) -> Invoice | None:
        return self.db.query(Invoice).filter(
            Invoice.id == invoice_id
        ).first()
