from decimal import Decimal

from app.utils.money import normalize_amount


def test_invoice_amount_normalization():
    amount = Decimal("10.456")
    normalized = normalize_amount(amount)
    assert normalized == Decimal("10.46")
