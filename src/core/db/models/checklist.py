from __future__ import annotations

import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base


class Checklist(Base):
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    task_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("task.id"), nullable=False, unique=True)

    task: Mapped["Task"] = relationship(back_populates="checklist", uselist=False)
    items: Mapped[list["ChecklistItem"]] = relationship(back_populates="checklist")
