from sqlalchemy.orm import Session

from app.domain.audit.models import AuditLog


class AuditRepository:
    def __init__(self, db: Session):
        self.db = db

    def log(self, entity_type: str, entity_id: int, action: str, metadata=None):
        entry = AuditLog(
            entity_type=entity_type,
            entity_id=entity_id,
            action=action,
            metadata=metadata,
        )
        self.db.add(entry)
        self.db.commit()
