from dataclasses import dataclass
from uuid import UUID


@dataclass
class TaskTagDTO:
    task_id: UUID
    label_id: UUID
