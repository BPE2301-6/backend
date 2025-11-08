import uuid

from src.core.db.models import Checklist
from ..base import BaseRepository

class ChecklistRepositoryImpl(BaseRepository[Checklist]):
    async def get_by_id(self, checklist_id: uuid.UUID) -> Checklist | None:
        return await self._db_get(Checklist, checklist_id)
    
    async def create(self, data: dict) -> Checklist:
        item = Checklist(**data)
        return await self._db_add(item)
    
    async def update(self, checklist_id: uuid.UUID, data: dict) -> Checklist:
        item = await self._db_get(Checklist, checklist_id)
        if item is None:
            return None
        return await self._db_update(item, data)

    async def delete(self, checklist_id: uuid.UUID) -> None:
        item = await self._db_get(Checklist, checklist_id)
        if item is not None:
            await self._db_delete(item)
