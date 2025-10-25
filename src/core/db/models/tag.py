from sqlalchemy import Column, String, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID

from ..base import Base


class Tag(Base):
    id = Column(UUID(as_uuid=True), primary_key=True)
    project_id = Column(UUID(as_uuid=True), ForeignKey("project.id"), nullable=False)
    name = Column(String(64), nullable=False)
    color = Column(String(7))

    __table_args__ = (
        UniqueConstraint("project_id", "name"),
    )
