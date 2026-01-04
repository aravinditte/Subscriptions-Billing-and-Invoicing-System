from decimal import Decimal

from app.services.invoice_service import InvoiceService


def test_invoice_creation(db_session):
    service = InvoiceService(db_session)

    invoice = service.create_invoice(
        subscription_id=1,
        amount=Decimal("99.99"),
        currency="USD",
    )

    assert invoice.amount == Decimal("99.99")
    assert invoice.status == "pending"
