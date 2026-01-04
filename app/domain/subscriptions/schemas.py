from pydantic import BaseModel
from datetime import datetime


class SubscriptionCreate(BaseModel):
    user_id: int
    plan_id: int
    start_date: datetime
    next_billing_date: datetime


class SubscriptionRead(BaseModel):
    id: int
    user_id: int
    plan_id: int
    status: str
    next_billing_date: datetime

    class Config:
        orm_mode = True
