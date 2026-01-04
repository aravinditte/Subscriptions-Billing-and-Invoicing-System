from sqlalchemy.orm import Session

from app.domain.plans.models import Plan


class PlanRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, **data) -> Plan:
        plan = Plan(**data)
        self.db.add(plan)
        self.db.commit()
        self.db.refresh(plan)
        return plan

    def get(self, plan_id: int) -> Plan | None:
        return self.db.query(Plan).filter(Plan.id == plan_id).first()
