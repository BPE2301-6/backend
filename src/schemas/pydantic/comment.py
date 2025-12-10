from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from .common import Paginated


class CommentRequest(BaseModel):
    body: str


class CommentResponse(BaseModel):
    id: UUID
    task_id: UUID
    author_id: UUID
    body: str
    created_at: datetime


class CommentListResponse(Paginated[CommentResponse]): ...
