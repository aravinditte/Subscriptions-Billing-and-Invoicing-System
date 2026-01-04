from app.exceptions.base import ApplicationError


class SubscriptionError(ApplicationError):
    """
    Raised for invalid subscription operations.
    """
