from sqlalchemy.orm import Session

from app.domain.audit.repository import AuditRepository


class AuditService:
    def __init__(self, db: Session):
        self.repo = AuditRepository(db)

    def log(
        self,
        entity_type: str,
        entity_id: int,
        action: str,
        metadata: dict | None = None,
    ) -> None:
        self.repo.log(
            entity_type=entity_type,
            entity_id=entity_id,
            action=action,
            metadata=metadata,
        )
