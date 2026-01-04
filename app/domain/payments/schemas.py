from pydantic import BaseModel
from decimal import Decimal


class PaymentRead(BaseModel):
    id: int
    invoice_id: int
    amount: Decimal
    status: str

    class Config:
        orm_mode = True
