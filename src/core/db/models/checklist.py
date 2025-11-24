from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base

if TYPE_CHECKING:
    from .checklist_item import ChecklistItem
    from .task import Task


class Checklist(Base):
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, server_default=text("gen_random_uuid()")
    )
    task_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("task.id", ondelete="CASCADE"), nullable=False, unique=True
    )

    task: Mapped[Task] = relationship(back_populates="checklist", uselist=False)
    items: Mapped[list[ChecklistItem]] = relationship(
        back_populates="checklist", passive_deletes=True
    )
