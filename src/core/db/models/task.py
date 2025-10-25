from sqlalchemy import (
    Column, String, Text, Integer, Date, DateTime, ForeignKey, Enum,
    UniqueConstraint, func
)
from sqlalchemy.dialects.postgresql import UUID
import enum

from ..base import Base


class TaskPriority(enum.Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class Task(Base):
    id = Column(UUID(as_uuid=True), primary_key=True)
    project_id = Column(UUID(as_uuid=True), ForeignKey("project.id"), nullable=False)
    seq = Column(Integer, nullable=False)
    key = Column(String(32), nullable=False, unique=True)
    title = Column(String(512), nullable=False)
    description = Column(Text)
    status_id = Column(UUID(as_uuid=True), ForeignKey("status.id"), nullable=False)
    priority = Column(Enum(TaskPriority), nullable=False, server_default="MEDIUM")
    reporter_id = Column(UUID(as_uuid=True), ForeignKey("usr.id"), nullable=False)
    assignee_id = Column(UUID(as_uuid=True), ForeignKey("usr.id"))
    due_date = Column(Date)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    __table_args__ = (
        UniqueConstraint("project_id", "seq"),
    )
