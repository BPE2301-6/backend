from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class ProjectMemberCreateRequest(BaseModel):
    user_id: UUID
    role: str


class ProjectMemberUpdateRequest(BaseModel):
    role: str


class ProjectMemberResponse(BaseModel):
    user_id: UUID
    role: str
    added_at: datetime
