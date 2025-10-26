from __future__ import annotations

import uuid

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base


class Tag(Base):
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("project.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(64), nullable=False)
    color: Mapped[str | None] = mapped_column(String(7))

    project: Mapped["Project"] = relationship(back_populates="tags")
    tasks: Mapped[list["TaskTag"]] = relationship(back_populates="tag")

    __table_args__ = (UniqueConstraint("project_id", "name"),)
