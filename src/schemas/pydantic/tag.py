from uuid import UUID

from pydantic import BaseModel

from .common import Paginated


class TagCreateRequest(BaseModel):
    name: str
    color: str | None = None


class TagUpdateRequest(BaseModel):
    name: str | None = None
    color: str | None = None


class TagResponse(BaseModel):
    id: UUID
    project_id: UUID
    name: str
    color: str | None


class TagListItem(BaseModel):
    id: UUID
    name: str
    color: str | None


class TagListResponse(Paginated[TagListItem]): ...
