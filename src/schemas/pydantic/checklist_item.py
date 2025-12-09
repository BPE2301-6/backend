from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field


class ChecklistItemCreateRequest(BaseModel):
    content: str
    position: int = Field(ge=0)


class ChecklistItemUpdateRequest(BaseModel):
    content: str | None = None
    is_done: bool | None = None
    position: int | None = Field(default=None, ge=0)


class ChecklistItemResponse(BaseModel):
    id: UUID
    content: str
    is_done: bool
    position: int
    created_at: datetime
