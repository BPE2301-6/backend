import uuid

from src.core.db import models
from ..base import BaseRepository


class ProjectMemberRepositoryImpl(BaseRepository[models.ProjectMember]):
    async def get(self, project_id: uuid.UUID, user_id: uuid.UUID) -> models.ProjectMember | None:
        return await self.session.get(models.ProjectMember, (project_id, user_id))

    async def create(self, data: dict) -> models.ProjectMember:
        item = models.ProjectMember(**data)
        return await self._db_add(item)

    async def update(self, project_id: uuid.UUID, user_id: uuid.UUID, data: dict) -> models.ProjectMember | None:
        item = await self.get(project_id, user_id)
        if item is None:
            return None
        return await self._db_update(item, data)

    async def delete(self, project_id: uuid.UUID, user_id: uuid.UUID) -> None:
        item = await self.get(project_id, user_id)
        if item is not None:
            await self._db_delete(item)

    async def list_by_project(self, project_id: uuid.UUID) -> list[models.ProjectMember]:
        return await self._db_list_by(models.ProjectMember, project_id=project_id)

    async def list_by_user(self, user_id: uuid.UUID) -> list[models.ProjectMember]:
        return await self._db_list_by(models.ProjectMember, user_id=user_id)
