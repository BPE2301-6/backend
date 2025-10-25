from sqlalchemy import Column, String, Boolean, Integer, DateTime, ForeignKey, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID

from ..base import Base


class ChecklistItem(Base):
    id = Column(UUID(as_uuid=True), primary_key=True)
    checklist_id = Column(UUID(as_uuid=True), ForeignKey("checklist.id"), nullable=False)
    content = Column(String(512), nullable=False)
    is_done = Column(Boolean, nullable=False, default=False)
    position = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    __table_args__ = (
        UniqueConstraint("checklist_id", "position"),
    )
