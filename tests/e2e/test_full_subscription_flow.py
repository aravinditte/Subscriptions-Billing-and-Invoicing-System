from datetime import datetime
from decimal import Decimal

from app.domain.users.repository import UserRepository
from app.domain.plans.repository import PlanRepository
from app.services.subscription_service import SubscriptionService
from app.services.billing_service import BillingService


def test_full_subscription_flow(db_session):
    user = UserRepository(db_session).create(
        email="e2e@example.com",
        name="E2E User",
    )

    plan = PlanRepository(db_session).create(
        name="Pro",
        price=Decimal("100.00"),
        currency="USD",
        interval="monthly",
    )

    subscription = SubscriptionService(db_session).create_subscription(
        user_id=user.id,
        plan_id=plan.id,
        start_date=datetime.utcnow(),
        next_billing_date=datetime.utcnow(),
    )

    billing = BillingService(db_session)
    invoice = billing.run_billing_cycle(subscription.id)

    assert invoice.subscription_id == subscription.id
