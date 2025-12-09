from dataclasses import dataclass
from uuid import UUID


@dataclass
class TagDTO:
    id: UUID
    project_id: UUID
    name: str
    color: str | None
