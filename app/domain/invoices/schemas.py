from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime


class InvoiceRead(BaseModel):
    id: int
    subscription_id: int
    amount: Decimal
    currency: str
    status: str
    issued_at: datetime

    class Config:
        orm_mode = True
