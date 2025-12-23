from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, String, Text, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base

if TYPE_CHECKING:
    from .project_member import ProjectMember
    from .status import Status
    from .tag import Tag
    from .task import Task
    from .task_sequence import TaskSequence
    from .user import User


class Project(Base):
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, server_default=text("gen_random_uuid()")
    )
    key: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    lead_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("usr.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
    )

    lead: Mapped[User] = relationship(back_populates="led_projects")
    members: Mapped[list[ProjectMember]] = relationship(
        back_populates="project", passive_deletes=True
    )
    tasks: Mapped[list[Task]] = relationship(back_populates="project", passive_deletes=True)
    statuses: Mapped[list[Status]] = relationship(back_populates="project", passive_deletes=True)
    tags: Mapped[list[Tag]] = relationship(back_populates="project", passive_deletes=True)
    task_sequence: Mapped[TaskSequence] = relationship(
        back_populates="project", uselist=False, passive_deletes=True
    )
