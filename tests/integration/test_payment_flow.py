from decimal import Decimal

from app.services.payment_service import PaymentService


def test_payment_creation(db_session):
    service = PaymentService(db_session)

    payment = service.charge_invoice(
        invoice_id=1,
        amount=Decimal("50.00"),
    )

    assert payment.amount == Decimal("50.00")
    assert payment.status in ("captured", "failed")
