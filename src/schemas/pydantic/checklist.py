from uuid import UUID

from pydantic import BaseModel


class ChecklistRequest(BaseModel):
    task_id: UUID


class ChecklistResponse(BaseModel):
    id: UUID
    task_id: UUID
