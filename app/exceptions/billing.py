from app.exceptions.base import ApplicationError


class BillingError(ApplicationError):
    """
    Raised when billing execution fails.
    """
