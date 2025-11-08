import uuid

from src.core.db import models
from ..base import BaseRepository


class CommentRepositoryImpl(BaseRepository[models.Comment]):
    async def get_by_id(self, comment_id: uuid.UUID) -> models.Comment | None:
        return await self._db_get(models.Comment, comment_id)

    async def create(self, data: dict) -> models.Comment:
        item = models.Comment(**data)
        return await self._db_add(item)

    async def update(self, comment_id: uuid.UUID, data: dict) -> models.Comment | None:
        item = await self._db_get(models.Comment, comment_id)
        if item is None:
            return None
        return await self._db_update(item, data)

    async def delete(self, comment_id: uuid.UUID) -> None:
        item = await self._db_get(models.Comment, comment_id)
        if item is not None:
            await self._db_delete(item)

    async def list_by_task_id(self, task_id: uuid.UUID) -> list[models.Comment]:
        return await self._db_list_by(models.Comment, task_id=task_id)
