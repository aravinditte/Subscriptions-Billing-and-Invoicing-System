from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.core.database import init_db
from app.core.logging import configure_logging
from app.api.v1 import users, plans, subscriptions, invoices, payments


def create_app() -> FastAPI:
    """
    Application factory.

    This pattern allows:
    - Easier testing
    - Clear initialization order
    - Future extensibility (multiple environments, workers, etc.)
    """

    settings = get_settings()

    app = FastAPI(
        title="Subscription Billing & Invoicing System",
        version="1.0.0",
        description=(
            "Enterprise-grade subscription billing and invoicing backend "
            "with recurring billing, audit logging, and payment simulation."
        ),
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # -------------------------
    # Logging
    # -------------------------
    configure_logging()

    # -------------------------
    # CORS (restricted by default)
    # -------------------------
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["Authorization", "Content-Type"],
    )

    # -------------------------
    # API Routers
    # -------------------------
    app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
    app.include_router(plans.router, prefix="/api/v1/plans", tags=["Plans"])
    app.include_router(
        subscriptions.router,
        prefix="/api/v1/subscriptions",
        tags=["Subscriptions"],
    )
    app.include_router(
        invoices.router,
        prefix="/api/v1/invoices",
        tags=["Invoices"],
    )
    app.include_router(
        payments.router,
        prefix="/api/v1/payments",
        tags=["Payments"],
    )

    return app


app = create_app()


@app.on_event("startup")
def on_startup() -> None:
    """
    Startup hook.

    Initializes database connections and ensures
    the application is ready to serve requests.
    """
    init_db()


@app.on_event("shutdown")
def on_shutdown() -> None:
    """
    Shutdown hook.

    Reserved for graceful shutdown logic such as:
    - Closing database connections
    - Flushing logs
    """
    pass
