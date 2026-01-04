from sqlalchemy.orm import Session

from app.domain.payments.models import Payment


class PaymentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, **data) -> Payment:
        payment = Payment(**data)
        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)
        return payment
