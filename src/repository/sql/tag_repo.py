import uuid
from src.core.db.models import Tag
from ..base import BaseRepository


class TagRepositoryImpl(BaseRepository[Tag]):
    async def get_by_id(self, tag_id: uuid.UUID) -> Tag | None:
        return await self._db_get(Tag, tag_id)

    async def create(self, data: dict) -> Tag:
        item = Tag(**data)
        return await self._db_add(item)

    async def update(self, tag_id: uuid.UUID, data: dict) -> Tag:
        item = await self._db_get(Tag, tag_id)
        if item is None:
            return None
        return await self._db_update(item, data)

    async def delete(self, tag_id: uuid.UUID) -> None:
        item = await self._db_get(Tag, tag_id)
        if item is not None:
            await self._db_delete(item)

    async def list_by_project(self, project_id: uuid.UUID) -> list[Tag]:
        return await self._db_list_by(Tag, project_id=project_id)
