from uuid import UUID
from pydantic import BaseModel


class ProjectCreateRequest(BaseModel):
    key: str
    name: str
    description: str | None = None
    lead_id: UUID


class ProjectUpdateRequest(BaseModel):
    name: str | None = None
    description: str | None = None
    lead_id: UUID | None = None


class ProjectResponse(BaseModel):
    id: UUID
    key: str
    name: str
    description: str | None
    lead_id: UUID
