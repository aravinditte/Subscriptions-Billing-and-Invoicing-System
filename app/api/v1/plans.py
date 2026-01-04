from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db_session
from app.domain.plans.schemas import PlanCreate, PlanRead
from app.domain.plans.repository import PlanRepository

router = APIRouter()


@router.post("/", response_model=PlanRead)
def create_plan(
    payload: PlanCreate,
    db: Session = Depends(get_db_session),
):
    repo = PlanRepository(db)
    return repo.create(**payload.dict())


@router.get("/{plan_id}", response_model=PlanRead)
def get_plan(
    plan_id: int,
    db: Session = Depends(get_db_session),
):
    repo = PlanRepository(db)
    return repo.get(plan_id)
