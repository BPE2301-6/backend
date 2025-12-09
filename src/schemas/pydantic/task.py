from typing import List
from uuid import UUID
from datetime import date
from pydantic import BaseModel

from .common import Paginated


class TaskCreateRequest(BaseModel):
    title: str
    description: str | None = None
    status_id: UUID
    priority: str
    reporter_id: UUID
    assignee_id: UUID | None = None
    due_date: date | None = None
    tag_ids: List[UUID] | None = None


class TaskUpdateRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    status_id: UUID | None = None
    priority: str | None = None
    assignee_id: UUID | None = None
    due_date: date | None = None


class TaskMoveRequest(BaseModel):
    status_id: UUID


class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: str | None
    status_id: UUID
    priority: str
    reporter_id: UUID
    assignee_id: UUID | None
    due_date: date | None
    tag_ids: List[UUID] | None = None


class TaskListResponse(Paginated[TaskResponse]): ...
