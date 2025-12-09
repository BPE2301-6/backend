import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import Checklist
from src.schemas.dtos import ChecklistDTO
from src.core.utils import map_model

from ..interfaces import BaseRepository


class ChecklistRepositoryImpl(BaseRepository[Checklist]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: uuid.UUID) -> ChecklistDTO | None:
        item = await Checklist.get_by_id(self.session, item_id)
        if item is None:
            return None
        return map_model(item, ChecklistDTO)

    async def create(self, data: dict) -> ChecklistDTO:
        item = Checklist.from_dict(data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, ChecklistDTO)

    async def update(self, item_id: uuid.UUID, data: dict) -> ChecklistDTO | None:
        item = await Checklist.get_by_id(self.session, item_id)
        if item is None:
            return None
        item.update(**data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, ChecklistDTO)

    async def delete(self, item_id: uuid.UUID) -> None:
        item = await Checklist.get_by_id(self.session, item_id)
        if item is not None:
            await item.delete(self.session)

    async def get_all(self) -> list[ChecklistDTO]:
        items = await Checklist.get_all(self.session)
        return [map_model(i, ChecklistDTO) for i in items]

    async def get_by_task_id(self, task_id: uuid.UUID) -> ChecklistDTO | None:
        stmt = select(Checklist).where(Checklist.task_id == task_id)
        result = await self.session.execute(stmt)
        item = result.scalars().first()
        if item is None:
            return None
        return map_model(item, ChecklistDTO)
