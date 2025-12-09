from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

from .common import Paginated


class CommentRequest(BaseModel):
    body: str


class CommentResponse(BaseModel):
    id: UUID
    task_id: UUID
    body: str
    created_at: datetime


class CommentListResponse(Paginated[CommentResponse]): ...
