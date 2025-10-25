from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID

from ..base import Base


class TaskTag(Base):
    task_id = Column(UUID(as_uuid=True), ForeignKey("task.id"), primary_key=True)
    tag_id = Column(UUID(as_uuid=True), ForeignKey("tag.id"), primary_key=True)

    __table_args__ = (
        UniqueConstraint("task_id", "tag_id"),
    )
