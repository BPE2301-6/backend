from __future__ import annotations

import enum
import uuid
from datetime import date, datetime

from sqlalchemy import String, Text, Integer, Date, DateTime, ForeignKey, Enum, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base


class TaskPriority(enum.Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class Task(Base):
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("project.id"), nullable=False)
    seq: Mapped[int] = mapped_column(Integer, nullable=False)
    key: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    title: Mapped[str] = mapped_column(String(512), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    status_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("status.id"), nullable=False)
    priority: Mapped[TaskPriority] = mapped_column(Enum(TaskPriority), nullable=False, server_default="MEDIUM")
    reporter_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("usr.id"), nullable=False)
    assignee_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("usr.id"))
    due_date: Mapped[date | None] = mapped_column(Date)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    project: Mapped["Project"] = relationship(back_populates="tasks")
    status: Mapped["Status"] = relationship(back_populates="tasks")
    reporter: Mapped["User"] = relationship(back_populates="reported_tasks", foreign_keys=[reporter_id])
    assignee: Mapped["User" | None] = relationship(back_populates="assigned_tasks", foreign_keys=[assignee_id])
    tags: Mapped[list["TaskTag"]] = relationship(back_populates="task")
    comments: Mapped[list["Comment"]] = relationship(back_populates="task")
    checklist: Mapped["Checklist" | None] = relationship(back_populates="task", uselist=False)

    __table_args__ = (
        UniqueConstraint("project_id", "seq"),
    )
