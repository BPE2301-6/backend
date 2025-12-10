from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class ChecklistItemDTO:
    id: UUID
    checklist_id: UUID
    content: str
    is_done: bool
    position: int
    created_at: datetime
