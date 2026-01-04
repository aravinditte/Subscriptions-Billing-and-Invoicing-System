from datetime import datetime

from sqlalchemy.orm import Session

from app.domain.subscriptions.repository import SubscriptionRepository
from app.domain.subscriptions.state_machine import SubscriptionStateMachine
from app.core.constants import SubscriptionStatus
from app.services.audit_service import AuditService


class SubscriptionService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = SubscriptionRepository(db)
        self.audit = AuditService(db)

    def create_subscription(
        self,
        user_id: int,
        plan_id: int,
        start_date: datetime,
        next_billing_date: datetime,
    ):
        subscription = self.repo.create(
            user_id=user_id,
            plan_id=plan_id,
            status=SubscriptionStatus.TRIAL,
            start_date=start_date,
            next_billing_date=next_billing_date,
        )

        self.audit.log(
            entity_type="subscription",
            entity_id=subscription.id,
            action="created",
        )

        return subscription

    def update_status(self, subscription_id: int, new_status: str):
        subscription = self.repo.get(subscription_id)

        if not subscription:
            raise ValueError("Subscription not found")

        if not SubscriptionStateMachine.can_transition(
            subscription.status, new_status
        ):
            raise ValueError(
                f"Invalid transition {subscription.status} -> {new_status}"
            )

        subscription.status = new_status
        self.db.commit()
        self.db.refresh(subscription)

        self.audit.log(
            entity_type="subscription",
            entity_id=subscription.id,
            action=f"status_changed_to_{new_status}",
        )

        return subscription
