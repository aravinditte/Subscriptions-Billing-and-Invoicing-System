from decimal import Decimal

from sqlalchemy.orm import Session

from app.domain.payments.repository import PaymentRepository
from app.domain.payments.gateway import MockPaymentGateway
from app.core.constants import PaymentStatus
from app.services.audit_service import AuditService


class PaymentService:
    def __init__(self, db: Session):
        self.repo = PaymentRepository(db)
        self.audit = AuditService(db)

    def charge_invoice(self, invoice_id: int, amount: Decimal):
        status, transaction_ref = MockPaymentGateway.charge(amount)

        payment = self.repo.create(
            invoice_id=invoice_id,
            amount=amount,
            status=status,
            transaction_ref=transaction_ref,
        )

        self.audit.log(
            entity_type="payment",
            entity_id=payment.id,
            action="attempted",
            metadata={
                "status": status,
                "transaction_ref": transaction_ref,
            },
        )

        return payment
