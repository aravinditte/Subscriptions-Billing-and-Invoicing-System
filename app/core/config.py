from functools import lru_cache
from typing import List

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.

    Uses Pydantic for validation and type safety.
    """

    APP_ENV: str = Field(default="development")
    APP_NAME: str = Field(default="subscription-billing-system")

    DATABASE_URL: str = Field(..., env="DATABASE_URL")

    REDIS_URL: str = Field(default="redis://redis:6379/0")

    SECRET_KEY: str = Field(..., env="SECRET_KEY")

    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=60)

    CORS_ORIGINS: List[str] = Field(default_factory=lambda: ["*"])

    BILLING_TIMEZONE: str = Field(default="UTC")

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """
    Cached settings accessor.

    Ensures settings are loaded only once per process.
    """
    return Settings()
