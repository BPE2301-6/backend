from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from ..enums import ProjectRole


@dataclass
class ProjectMemberDTO:
    project_id: UUID
    user_id: UUID
    role: ProjectRole
    added_at: datetime
