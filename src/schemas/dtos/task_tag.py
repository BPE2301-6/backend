from dataclasses import dataclass
from uuid import UUID


@dataclass
class TaskTagDTO:
    task_id: UUID
    tag_id: UUID
