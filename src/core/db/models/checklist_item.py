from __future__ import annotations
from typing import TYPE_CHECKING

import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base

if TYPE_CHECKING:
    from .checklist import Checklist


class ChecklistItem(Base):
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    checklist_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("checklist.id"), nullable=False)
    content: Mapped[str] = mapped_column(String(512), nullable=False)
    is_done: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default="false")
    position: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    checklist: Mapped[Checklist] = relationship(back_populates="items")

    __table_args__ = (UniqueConstraint("checklist_id", "position"),)
