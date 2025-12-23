from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel

from src.schemas.enums import TaskPriority, TimeDeltaStatus

from .common import Paginated


class TimeDelta(BaseModel):
    status: TimeDeltaStatus
    delta: float


class TaskCreateRequest(BaseModel):
    title: str
    description: str | None = None
    status_id: UUID
    priority: TaskPriority
    reporter_id: UUID
    assignee_id: UUID | None = None
    due_date: date | None = None
    tag_ids: list[UUID] | None = None


class TaskUpdateRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    status_id: UUID | None = None
    priority: TaskPriority | None = None
    assignee_id: UUID | None = None
    due_date: date | None = None


class TaskMoveRequest(BaseModel):
    status_id: UUID


class TaskResponse(BaseModel):
    id: UUID
    project_id: UUID
    seq: int
    key: str
    title: str
    description: str | None
    status_id: UUID
    priority: TaskPriority
    reporter_id: UUID
    assignee_id: UUID | None
    due_date: date | None
    created_at: datetime
    updated_at: datetime
    timedelta: TimeDelta


class TaskListResponse(Paginated[TaskResponse]): ...
