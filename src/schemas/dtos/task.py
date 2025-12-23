from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from ..enums import TaskPriority, TimeDeltaStatus


@dataclass
class TimeDeltaDTO:
    status: TimeDeltaStatus
    delta: float


@dataclass
class TaskDTO:
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
    due_date: datetime | None
    created_at: datetime
    updated_at: datetime
    timedelta: TimeDeltaDTO | None = None
