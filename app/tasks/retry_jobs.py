from sqlalchemy.orm import Session

from app.tasks.celery_app import celery_app
from app.core.database import SessionLocal
from app.services.billing_service import BillingService
from app.domain.subscriptions.repository import SubscriptionRepository
from app.core.constants import SubscriptionStatus


@celery_app.task
def retry_past_due_subscriptions():
    """
    Retries billing for subscriptions in PAST_DUE state.
    """
    db: Session = SessionLocal()
    try:
        repo = SubscriptionRepository(db)
        service = BillingService(db)

        subscriptions = (
            db.query(repo.db.bind.mapper_registry.mapped_classes.pop())
        )

        for sub in subscriptions:
            if sub.status == SubscriptionStatus.PAST_DUE:
                service.run_billing_cycle(sub.id)
    finally:
        db.close()
