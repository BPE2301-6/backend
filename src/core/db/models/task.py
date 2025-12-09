from __future__ import annotations

import uuid
from datetime import date, datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    Date,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.schemas.enums import TaskPriority
from ..base import Base

if TYPE_CHECKING:
    from .checklist import Checklist
    from .comment import Comment
    from .project import Project
    from .status import Status
    from .task_tag import TaskTag
    from .user import User


class Task(Base):
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, server_default=text("gen_random_uuid()")
    )
    project_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("project.id", ondelete="CASCADE"), nullable=False
    )
    seq: Mapped[int] = mapped_column(Integer, nullable=False)
    key: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    title: Mapped[str] = mapped_column(String(512), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    status_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("status.id", ondelete="RESTRICT"), nullable=False
    )
    priority: Mapped[TaskPriority] = mapped_column(
        Enum(TaskPriority), nullable=False, server_default="MEDIUM"
    )
    reporter_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("usr.id"), nullable=False)
    assignee_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("usr.id"))
    due_date: Mapped[date | None] = mapped_column(Date)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    project: Mapped[Project] = relationship(back_populates="tasks")
    status: Mapped[Status] = relationship(back_populates="tasks")
    reporter: Mapped[User] = relationship(
        back_populates="reported_tasks", foreign_keys=[reporter_id]
    )
    assignee: Mapped[User | None] = relationship(
        back_populates="assigned_tasks", foreign_keys=[assignee_id]
    )
    tags: Mapped[list[TaskTag]] = relationship(back_populates="task", passive_deletes=True)
    comments: Mapped[list[Comment]] = relationship(back_populates="task", passive_deletes=True)
    checklist: Mapped[Checklist | None] = relationship(
        back_populates="task", uselist=False, passive_deletes=True
    )

    __table_args__ = (UniqueConstraint("project_id", "seq"),)
