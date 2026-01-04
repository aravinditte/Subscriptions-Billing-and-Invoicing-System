from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.sql import func

from app.core.database import Base
from app.core.constants import SubscriptionStatus


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    plan_id = Column(Integer, ForeignKey("plans.id"), nullable=False)

    status = Column(
        String(20),
        nullable=False,
        default=SubscriptionStatus.TRIAL,
    )

    start_date = Column(DateTime(timezone=True), nullable=False)
    end_date = Column(DateTime(timezone=True), nullable=True)
    next_billing_date = Column(DateTime(timezone=True), nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
