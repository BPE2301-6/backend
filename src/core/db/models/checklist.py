from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from ..base import Base


class Checklist(Base):
    id = Column(UUID(as_uuid=True), primary_key=True)
    task_id = Column(UUID(as_uuid=True), ForeignKey("task.id"), nullable=False, unique=True)
