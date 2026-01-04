from typing import Generator

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import create_access_token


def get_db_session() -> Generator[Session, None, None]:
    """
    Database dependency for FastAPI routes.
    """
    yield from get_db()


def create_internal_token(subject: str) -> str:
    """
    Utility for creating internal/admin tokens.
    """
    return create_access_token(subject=subject)
