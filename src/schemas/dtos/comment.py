from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class CommentDTO:
    id: UUID
    task_id: UUID
    author_id: UUID
    body: str
    created_at: datetime
