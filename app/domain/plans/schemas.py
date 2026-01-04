from pydantic import BaseModel
from decimal import Decimal


class PlanCreate(BaseModel):
    name: str
    price: Decimal
    currency: str
    interval: str


class PlanRead(BaseModel):
    id: int
    name: str
    price: Decimal
    currency: str
    interval: str

    class Config:
        orm_mode = True
