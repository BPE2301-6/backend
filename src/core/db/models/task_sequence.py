from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base

if TYPE_CHECKING:
    from .project import Project


class TaskSequence(Base):
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("project.id", ondelete="CASCADE"), primary_key=True)
    next_seq: Mapped[int] = mapped_column(Integer, nullable=False, server_default="1")

    project: Mapped[Project] = relationship(back_populates="task_sequence", uselist=False)
