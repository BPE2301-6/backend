from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base

if TYPE_CHECKING:
    from .comment import Comment
    from .project import Project
    from .project_member import ProjectMember
    from .task import Task


class User(Base):
    __tablename__ = "usr"  # Так как user - зарезервированное слово в PostgreSQL

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    avatar_url: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    led_projects: Mapped[list[Project]] = relationship(back_populates="lead")
    projects: Mapped[list[ProjectMember]] = relationship(back_populates="user")
    reported_tasks: Mapped[list[Task]] = relationship(
        back_populates="reporter", foreign_keys="[Task.reporter_id]"
    )
    assigned_tasks: Mapped[list[Task]] = relationship(
        back_populates="assignee", foreign_keys="[Task.assignee_id]"
    )
    comments: Mapped[list[Comment]] = relationship(back_populates="author")
