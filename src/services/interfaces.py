import uuid
from typing import Protocol, TypeVar, Tuple, Generic, Any

T = TypeVar("T")


class BaseService(Protocol, Generic[T]):
    async def get(self, item_id: uuid.UUID | Tuple[uuid.UUID, uuid.UUID]) -> T | None: ...
    async def create(self, data: dict) -> T: ...
    async def update(self, item_id: uuid.UUID | Tuple[uuid.UUID, uuid.UUID], data: dict) -> T: ...
    async def delete(self, item_id: uuid.UUID | Tuple[uuid.UUID, uuid.UUID]) -> None: ...
    async def get_all(self) -> list[T]: ...


class Service(Protocol):
    checklist_items: BaseService[Any]
    checklists: BaseService[Any]
    comments: BaseService[Any]
    project_members: BaseService[Any]
    projects: BaseService[Any]
    statuses: BaseService[Any]
    tags: BaseService[Any]
    tasks: BaseService[Any]
    task_sequences: BaseService[Any]
    task_tags: BaseService[Any]
    users: BaseService[Any]
