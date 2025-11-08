from __future__ import annotations
from typing import TYPE_CHECKING

import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base

if TYPE_CHECKING:
    from .user import User
    from .project_member import ProjectMember
    from .task import Task
    from .status import Status
    from .tag import Tag
    from .task_sequence import TaskSequence


class Project(Base):
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    key: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    lead_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("usr.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    lead: Mapped[User] = relationship(back_populates="led_projects")
    members: Mapped[list[ProjectMember]] = relationship(back_populates="project")
    tasks: Mapped[list[Task]] = relationship(back_populates="project")
    statuses: Mapped[list[Status]] = relationship(back_populates="project")
    tags: Mapped[list[Tag]] = relationship(back_populates="project")
    task_sequence: Mapped[TaskSequence] = relationship(back_populates="project", uselist=False)
