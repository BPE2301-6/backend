from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base

if TYPE_CHECKING:
    from .tag import Tag
    from .task import Task


class TaskTag(Base):
    task_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("task.id"), primary_key=True)
    tag_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("tag.id"), primary_key=True)

    task: Mapped[Task] = relationship(back_populates="tags")
    tag: Mapped[Tag] = relationship(back_populates="tasks")

    __table_args__ = (UniqueConstraint("task_id", "tag_id"),)
