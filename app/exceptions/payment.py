from app.exceptions.base import ApplicationError


class PaymentError(ApplicationError):
    """
    Raised when payment processing fails.
    """
