from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class StatusDTO:
    id: UUID
    project_id: UUID
    name: str
    position: int
    is_closed: bool
    created_at: datetime
