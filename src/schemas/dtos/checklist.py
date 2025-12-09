from dataclasses import dataclass
from uuid import UUID


@dataclass
class ChecklistDTO:
    id: UUID
    task_id: UUID
