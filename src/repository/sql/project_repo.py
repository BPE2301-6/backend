import uuid

from src.core.db.models import Project
from ..base import BaseRepository


class ProjectRepositoryImpl(BaseRepository[Project]):
    async def get_by_id(self, project_id: uuid.UUID) -> Project | None:
        return await self._db_get(Project, project_id)

    async def create(self, data: dict) -> Project:
        item = Project(**data)
        return await self._db_add(item)

    async def update(self, project_id: uuid.UUID, data: dict) -> Project:
        item = await self._db_get(Project, project_id)
        if item is None:
            return None
        return await self._db_update(item, data)

    async def delete(self, project_id: uuid.UUID) -> None:
        item = await self._db_get(Project, project_id)
        if item is not None:
            await self._db_delete(item)
