from uuid import UUID
from pydantic import BaseModel


class TaskTagRequest(BaseModel):
    tag_ids: list[UUID]


class TaskTagResponse(BaseModel):
    tag_ids: list[UUID]
