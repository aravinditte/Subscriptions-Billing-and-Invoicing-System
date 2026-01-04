from datetime import datetime, timedelta
from decimal import Decimal

from app.services.billing_service import BillingService
from app.domain.users.repository import UserRepository
from app.domain.plans.repository import PlanRepository
from app.domain.subscriptions.repository import SubscriptionRepository
from app.core.constants import SubscriptionStatus


def test_billing_cycle_success_or_failure(db_session):
    user = UserRepository(db_session).create(
        email="test@example.com",
        name="Test User",
    )

    plan = PlanRepository(db_session).create(
        name="Basic",
        price=Decimal("20.00"),
        currency="USD",
        interval="monthly",
    )

    subscription = SubscriptionRepository(db_session).create(
        user_id=user.id,
        plan_id=plan.id,
        status=SubscriptionStatus.ACTIVE,
        start_date=datetime.utcnow(),
        next_billing_date=datetime.utcnow(),
    )

    service = BillingService(db_session)
    invoice = service.run_billing_cycle(subscription.id)

    assert invoice is not None
