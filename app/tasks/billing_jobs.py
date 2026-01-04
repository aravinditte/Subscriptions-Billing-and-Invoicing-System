from sqlalchemy.orm import Session

from app.tasks.celery_app import celery_app
from app.core.database import SessionLocal
from app.services.billing_service import BillingService


@celery_app.task(bind=True, autoretry_for=(Exception,), retry_backoff=60, retry_kwargs={"max_retries": 3})
def run_subscription_billing(self, subscription_id: int):
    """
    Executes billing for a single subscription.
    Safe to retry due to idempotent billing design.
    """
    db: Session = SessionLocal()
    try:
        service = BillingService(db)
        return service.run_billing_cycle(subscription_id)
    finally:
        db.close()
