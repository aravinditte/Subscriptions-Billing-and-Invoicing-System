from datetime import timedelta

from sqlalchemy.orm import Session

from app.domain.subscriptions.repository import SubscriptionRepository
from app.domain.plans.repository import PlanRepository
from app.services.invoice_service import InvoiceService
from app.services.payment_service import PaymentService
from app.services.subscription_service import SubscriptionService
from app.core.constants import SubscriptionStatus, PaymentStatus
from app.utils.time import utcnow


class BillingService:
    """
    Coordinates the recurring billing process.
    """

    def __init__(self, db: Session):
        self.db = db
        self.sub_repo = SubscriptionRepository(db)
        self.plan_repo = PlanRepository(db)
        self.invoice_service = InvoiceService(db)
        self.payment_service = PaymentService(db)
        self.subscription_service = SubscriptionService(db)

    def run_billing_cycle(self, subscription_id: int):
        subscription = self.sub_repo.get(subscription_id)

        if not subscription:
            raise ValueError("Subscription not found")

        if subscription.status not in (
            SubscriptionStatus.ACTIVE,
            SubscriptionStatus.TRIAL,
        ):
            return None

        plan = self.plan_repo.get(subscription.plan_id)

        invoice = self.invoice_service.create_invoice(
            subscription_id=subscription.id,
            amount=plan.price,
            currency=plan.currency,
        )

        payment = self.payment_service.charge_invoice(
            invoice_id=invoice.id,
            amount=invoice.amount,
        )

        if payment.status == PaymentStatus.CAPTURED:
            self.invoice_service.mark_paid(invoice.id)
            self.subscription_service.update_status(
                subscription.id,
                SubscriptionStatus.ACTIVE,
            )
            subscription.next_billing_date += timedelta(days=30)
        else:
            self.invoice_service.mark_failed(invoice.id)
            self.subscription_service.update_status(
                subscription.id,
                SubscriptionStatus.PAST_DUE,
            )

        self.db.commit()
        return invoice
