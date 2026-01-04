from sqlalchemy import Column, Integer, String, Numeric

from app.core.database import Base
from app.core.constants import BillingInterval


class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    currency = Column(String(10), nullable=False)
    interval = Column(String(20), nullable=False, default=BillingInterval.MONTHLY)
