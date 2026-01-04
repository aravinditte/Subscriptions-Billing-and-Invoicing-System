from sqlalchemy.orm import Session

from app.domain.subscriptions.models import Subscription


class SubscriptionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, **data) -> Subscription:
        sub = Subscription(**data)
        self.db.add(sub)
        self.db.commit()
        self.db.refresh(sub)
        return sub

    def get(self, subscription_id: int) -> Subscription | None:
        return self.db.query(Subscription).filter(
            Subscription.id == subscription_id
        ).first()
