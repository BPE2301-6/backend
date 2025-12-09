from uuid import UUID
from pydantic import BaseModel

from .common import Paginated


class TagCreateRequest(BaseModel):
    name: str
    color: str


class TagUpdateRequest(BaseModel):
    name: str | None = None
    color: str | None = None


class TagResponse(BaseModel):
    id: UUID
    project_id: UUID
    name: str
    color: str


class TagListResponse(Paginated[TagResponse]): ...
