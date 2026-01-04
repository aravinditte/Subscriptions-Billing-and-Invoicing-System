class ApplicationError(Exception):
    """
    Base exception for all application-level errors.
    """

    def __init__(self, message: str):
        super().__init__(message)
