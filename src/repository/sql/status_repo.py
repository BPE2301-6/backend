import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import Status
from src.schemas.dtos import StatusDTO
from src.core.utils import map_model

from ..interfaces import BaseRepository


class StatusRepositoryImpl(BaseRepository[Status]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: uuid.UUID) -> StatusDTO | None:
        item = await Status.get_by_id(self.session, item_id)
        if item is None:
            return None
        return map_model(item, StatusDTO)

    async def create(self, data: dict) -> StatusDTO:
        item = Status.from_dict(data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, StatusDTO)

    async def update(self, item_id: uuid.UUID, data: dict) -> StatusDTO | None:
        item = await Status.get_by_id(self.session, item_id)
        if item is None:
            return None
        item.update(**data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, StatusDTO)

    async def delete(self, item_id: uuid.UUID) -> None:
        item = await Status.get_by_id(self.session, item_id)
        if item is not None:
            await item.delete(self.session)

    async def get_all(self) -> list[StatusDTO]:
        items = await Status.get_all(self.session)
        return [map_model(i, StatusDTO) for i in items]

    async def get_all_by_project(self, project_id: uuid.UUID) -> list[StatusDTO]:
        stmt = select(Status).where(Status.project_id == project_id).order_by(Status.position.asc())
        result = await self.session.execute(stmt)
        items = result.scalars().all()
        return [map_model(i, StatusDTO) for i in items]
