from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class StatusCreateRequest(BaseModel):
    name: str
    position: int = Field(ge=0)
    is_closed: bool


class StatusUpdateRequest(BaseModel):
    name: str | None = None
    position: int | None = Field(default=None, ge=0)
    is_closed: bool | None = None


class StatusResponse(BaseModel):
    id: UUID
    project_id: UUID
    name: str
    position: int
    is_closed: bool
    created_at: datetime
