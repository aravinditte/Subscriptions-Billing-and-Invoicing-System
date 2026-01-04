from decimal import Decimal, ROUND_HALF_UP


def normalize_amount(amount: Decimal) -> Decimal:
    """
    Normalizes monetary values to two decimal places.
    """
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
