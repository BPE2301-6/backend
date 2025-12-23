from datetime import UTC, datetime
from uuid import UUID

from src.repository import Store
from src.schemas.dtos import TaskDTO, TimeDeltaDTO
from src.schemas.enums import TimeDeltaStatus

from ..interfaces import BaseService


class TaskServiceImpl(BaseService[TaskDTO]):
    def __init__(self, store: Store):
        self.store = store

    def _build_timedelta(self, updated_at: datetime) -> TimeDeltaDTO:
        now = datetime.now(UTC)
        seconds_passed = (now - updated_at).total_seconds()
        week_seconds = 7 * 24 * 3600

        percent = min(100, 100 * (seconds_passed / week_seconds))

        days_passed = seconds_passed / 86400
        if days_passed < 3:
            status = TimeDeltaStatus.LOW
        elif days_passed <= 5:
            status = TimeDeltaStatus.MEDIUM
        else:
            status = TimeDeltaStatus.HIGH

        return TimeDeltaDTO(status=status, delta=percent)

    async def get(self, item_id: UUID) -> TaskDTO | None:
        item = await self.store.task_repo().get_by_id(item_id)
        if item:
            item.timedelta = self._build_timedelta(item.updated_at)
        return item

    async def create(self, data: dict) -> TaskDTO:
        tag_ids = data.pop("tag_ids", None)

        project_id: UUID = data["project_id"]
        project_key = await self.store.project_repo().get_key_by_id(project_id)
        seq = await self.store.task_sequence_repo().reserve_next_seq(project_id)

        data["seq"] = seq
        data["key"] = f"{project_key}-{seq}"

        item = await self.store.task_repo().create(data)
        item.timedelta = self._build_timedelta(item.updated_at)

        if tag_ids:
            for tag_id in tag_ids:
                await self.store.task_tag_repo().create({"task_id": item.id, "tag_id": tag_id})

        return item

    async def update(self, item_id: UUID, data: dict) -> TaskDTO:
        item = await self.store.task_repo().update(item_id, data)
        if item:
            item.timedelta = self._build_timedelta(item.updated_at)
        return item

    async def delete(self, item_id: UUID) -> None:
        await self.store.task_repo().delete(item_id)

    async def get_all(self) -> list[TaskDTO]:
        items = await self.store.task_repo().get_all()
        for item in items:
            item.timedelta = self._build_timedelta(item.updated_at)
        return items

    async def get_all_by_project(
        self, project_id: UUID, filters: dict, limit: int, offset: int, sort: str
    ) -> tuple[list[TaskDTO], int]:
        items, total = await self.store.task_repo().get_all_by_project(
            project_id, filters, limit, offset, sort
        )
        for item in items:
            item.timedelta = self._build_timedelta(item.updated_at)
        return items, total
