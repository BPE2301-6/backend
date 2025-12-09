from dataclasses import dataclass
from uuid import UUID


@dataclass
class TaskSequenceDTO:
    project_id: UUID
    next_seq: int
