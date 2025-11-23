from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base

if TYPE_CHECKING:
    from .project import Project
    from .task_tag import TaskTag


class Tag(Base):
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, server_default=text("gen_random_uuid()"))
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("project.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String(64), nullable=False)
    color: Mapped[str | None] = mapped_column(String(7))

    project: Mapped[Project] = relationship(back_populates="tags")
    tasks: Mapped[list[TaskTag]] = relationship(back_populates="tag", passive_deletes=True)

    __table_args__ = (UniqueConstraint("project_id", "name"),)
