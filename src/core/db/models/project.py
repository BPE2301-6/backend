from sqlalchemy import Column, String, Text, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID

from ..base import Base


class Project(Base):
    id = Column(UUID(as_uuid=True), primary_key=True)
    key = Column(String(10), nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    lead_id = Column(UUID(as_uuid=True), ForeignKey("usr.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
