from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base


class Comment(Base):
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    task_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("task.id"), nullable=False)
    author_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("usr.id"), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    task: Mapped["Task"] = relationship(back_populates="comments")
    author: Mapped["User"] = relationship(back_populates="comments")
