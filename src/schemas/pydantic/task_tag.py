from uuid import UUID
from pydantic import BaseModel
from typing import list


class TaskTagRequest(BaseModel):
    tag_ids: list[UUID]


class TaskTagResponse(BaseModel):
    tag_ids: list[UUID]
