from __future__ import annotations

import enum
import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base

if TYPE_CHECKING:
    from .project import Project
    from .user import User


class ProjectRole(enum.Enum):
    OWNER = "OWNER"
    MEMBER = "MEMBER"


class ProjectMember(Base):
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("project.id", ondelete="CASCADE"), primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("usr.id"), primary_key=True)
    role: Mapped[ProjectRole] = mapped_column(
        Enum(ProjectRole), nullable=False, server_default="MEMBER"
    )
    added_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    project: Mapped[Project] = relationship(back_populates="members")
    user: Mapped[User] = relationship(back_populates="projects")

    __table_args__ = (UniqueConstraint("project_id", "user_id"),)
