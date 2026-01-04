import random
import uuid

from app.core.constants import PaymentStatus


class MockPaymentGateway:
    """
    Simulated payment gateway for development and testing.
    """

    @staticmethod
    def charge(amount) -> tuple[str, str]:
        success = random.choice([True, False])

        if success:
            return PaymentStatus.CAPTURED, str(uuid.uuid4())

        return PaymentStatus.FAILED, str(uuid.uuid4())
