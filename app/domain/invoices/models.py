from sqlalchemy import Column, Integer, ForeignKey, Numeric, String, DateTime
from sqlalchemy.sql import func

from app.core.database import Base
from app.core.constants import InvoiceStatus


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)
    subscription_id = Column(Integer, ForeignKey("subscriptions.id"), nullable=False)

    amount = Column(Numeric(10, 2), nullable=False)
    currency = Column(String(10), nullable=False)
    status = Column(String(20), nullable=False, default=InvoiceStatus.PENDING)

    issued_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
