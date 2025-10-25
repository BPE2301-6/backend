from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from ..base import Base


class TaskSequence(Base):
    project_id = Column(UUID(as_uuid=True), ForeignKey("project.id"), primary_key=True)
    next_seq = Column(Integer, nullable=False, default=1)
