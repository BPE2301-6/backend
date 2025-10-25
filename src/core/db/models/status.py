from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID

from ..base import Base


class Status(Base):
    id = Column(UUID(as_uuid=True), primary_key=True)
    project_id = Column(UUID(as_uuid=True), ForeignKey("project.id"), nullable=False)
    name = Column(String(64), nullable=False)
    position = Column(Integer, nullable=False, default=0)
    is_closed = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

__table_args__ = (
    UniqueConstraint("project_id", "name"),
    UniqueConstraint("project_id", "position"),
)
