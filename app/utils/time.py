from datetime import datetime, timezone


def utcnow() -> datetime:
    """
    Returns the current UTC time with timezone awareness.
    """
    return datetime.now(timezone.utc)
