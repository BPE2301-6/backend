from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from ..enums import ProjectRole


class ProjectMemberCreateRequest(BaseModel):
    user_id: UUID
    role: ProjectRole


class ProjectMemberUpdateRequest(BaseModel):
    role: ProjectRole


class ProjectMemberResponse(BaseModel):
    user_id: UUID
    role: ProjectRole
    added_at: datetime
