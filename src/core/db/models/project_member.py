from sqlalchemy import Column, Enum, DateTime, ForeignKey, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
import enum

from ..base import Base


class ProjectRole(enum.Enum):
    OWNER = "OWNER"
    MEMBER = "MEMBER"


class ProjectMember(Base):
    project_id = Column(UUID(as_uuid=True), ForeignKey("project.id"), nullable=False, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("usr.id"), nullable=False, primary_key=True)
    role = Column(Enum(ProjectRole), nullable=False, server_default="MEMBER")
    added_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    __table_args__ = (
        UniqueConstraint("project_id", "user_id"),
    )
