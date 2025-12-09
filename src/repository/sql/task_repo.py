import uuid
from datetime import datetime
from sqlalchemy import and_, asc, desc, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import Task, TaskTag
from src.schemas.dtos import TaskDTO
from src.core.utils import map_model

from ..interfaces import BaseRepository


class TaskRepositoryImpl(BaseRepository[Task]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: uuid.UUID) -> TaskDTO | None:
        item = await Task.get_by_id(self.session, item_id)
        if item is None:
            return None
        return map_model(item, TaskDTO)

    async def create(self, data: dict) -> TaskDTO:
        item = Task.from_dict(data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, TaskDTO)

    async def update(self, item_id: uuid.UUID, data: dict) -> TaskDTO | None:
        item = await Task.get_by_id(self.session, item_id)
        if item is None:
            return None
        item.update(**data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, TaskDTO)

    async def delete(self, item_id: uuid.UUID) -> None:
        item = await Task.get_by_id(self.session, item_id)
        if item is not None:
            await item.delete(self.session)

    async def get_all(self) -> list[TaskDTO]:
        items = await Task.get_all(self.session)
        return [map_model(i, TaskDTO) for i in items]

    async def get_all_by_project(
        self, project_id: uuid.UUID, filters: dict, limit: int, offset: int, sort: str
    ) -> tuple[list[TaskDTO], int]:
        stmt = select(Task).where(Task.project_id == project_id)

        filter_conditions = []
        if "status_id" in filters:
            filter_conditions.append(Task.status_id == filters["status_id"])
        if "assignee_id" in filters:
            filter_conditions.append(Task.assignee_id == filters["assignee_id"])
        if "reporter_id" in filters:
            filter_conditions.append(Task.reporter_id == filters["reporter_id"])
        if "priority" in filters:
            filter_conditions.append(Task.priority == filters["priority"])
        if "tag_id" in filters:
            stmt = stmt.join(Task.tags).where(TaskTag.tag_id == filters["tag_id"])
        if "q" in filters:
            q = f"%{filters['q']}%"
            filter_conditions.append(or_(Task.title.ilike(q), Task.description.ilike(q)))
        if "due_from" in filters and filters["due_from"]:
            due_from = datetime.fromisoformat(filters["due_from"])
            filter_conditions.append(Task.due_date >= due_from)
        if "due_to" in filters and filters["due_to"]:
            due_to = datetime.fromisoformat(filters["due_to"])
            filter_conditions.append(Task.due_date <= due_to)

        if filter_conditions:
            stmt = stmt.where(and_(*filter_conditions))

        if sort.startswith("-"):
            stmt = stmt.order_by(desc(getattr(Task, sort[1:], Task.created_at)))
        else:
            stmt = stmt.order_by(asc(getattr(Task, sort, Task.created_at)))

        stmt = stmt.offset(offset).limit(limit)
        result = await self.session.execute(stmt)
        items = result.scalars().all()
        dto_items = [map_model(i, TaskDTO) for i in items]

        count_stmt = select(func.count()).select_from(Task).where(Task.project_id == project_id)
        if filter_conditions:
            count_stmt = count_stmt.where(and_(*filter_conditions))
        total_result = await self.session.execute(count_stmt)
        total = total_result.scalar_one()

        return dto_items, total
