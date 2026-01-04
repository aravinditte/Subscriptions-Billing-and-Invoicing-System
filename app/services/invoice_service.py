from decimal import Decimal

from sqlalchemy.orm import Session

from app.domain.invoices.repository import InvoiceRepository
from app.services.audit_service import AuditService
from app.core.constants import InvoiceStatus


class InvoiceService:
    def __init__(self, db: Session):
        self.repo = InvoiceRepository(db)
        self.audit = AuditService(db)

    def create_invoice(
        self,
        subscription_id: int,
        amount: Decimal,
        currency: str,
    ):
        invoice = self.repo.create(
            subscription_id=subscription_id,
            amount=amount,
            currency=currency,
            status=InvoiceStatus.PENDING,
        )

        self.audit.log(
            entity_type="invoice",
            entity_id=invoice.id,
            action="created",
            metadata={"amount": str(amount), "currency": currency},
        )

        return invoice

    def mark_paid(self, invoice_id: int):
        invoice = self.repo.get(invoice_id)

        if not invoice:
            raise ValueError("Invoice not found")

        invoice.status = InvoiceStatus.PAID
        self.repo.db.commit()
        self.repo.db.refresh(invoice)

        self.audit.log(
            entity_type="invoice",
            entity_id=invoice.id,
            action="marked_paid",
        )

        return invoice

    def mark_failed(self, invoice_id: int):
        invoice = self.repo.get(invoice_id)

        if not invoice:
            raise ValueError("Invoice not found")

        invoice.status = InvoiceStatus.FAILED
        self.repo.db.commit()
        self.repo.db.refresh(invoice)

        self.audit.log(
            entity_type="invoice",
            entity_id=invoice.id,
            action="marked_failed",
        )

        return invoice
