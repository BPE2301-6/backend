from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class ProjectDTO:
    id: UUID
    key: str
    name: str
    description: str | None
    lead_id: UUID
    created_at: datetime
    updated_at: datetime
