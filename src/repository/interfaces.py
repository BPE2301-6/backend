import uuid
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from src.core.db import Base

T = TypeVar("T", bound=Base)


# noinspection DuplicatedCode
class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    async def get_by_id(self, item_id: uuid.UUID | tuple[uuid.UUID, uuid.UUID]) -> T | None: ...

    @abstractmethod
    async def create(self, data: dict) -> T: ...

    @abstractmethod
    async def update(self, item_id: uuid.UUID | tuple[uuid.UUID, uuid.UUID], data: dict) -> T: ...

    @abstractmethod
    async def delete(self, item_id: uuid.UUID | tuple[uuid.UUID, uuid.UUID]) -> None: ...

    @abstractmethod
    async def get_all(self) -> list[T]: ...


class Store(ABC):
    checklist_items: BaseRepository[...]
    checklists: BaseRepository[...]
    comments: BaseRepository[...]
    project_members: BaseRepository[...]
    projects: BaseRepository[...]
    statuses: BaseRepository[...]
    tags: BaseRepository[...]
    tasks: BaseRepository[...]
    task_sequences: BaseRepository[...]
    task_tags: BaseRepository[...]
    users: BaseRepository[...]

    @abstractmethod
    def checklist_item_repo(self) -> BaseRepository[...]: ...

    @abstractmethod
    def checklist_repo(self) -> BaseRepository[...]: ...

    @abstractmethod
    def comment_repo(self) -> BaseRepository[...]: ...

    @abstractmethod
    def project_member_repo(self) -> BaseRepository[...]: ...

    @abstractmethod
    def project_repo(self) -> BaseRepository[...]: ...

    @abstractmethod
    def status_repo(self) -> BaseRepository[...]: ...

    @abstractmethod
    def tag_repo(self) -> BaseRepository[...]: ...

    @abstractmethod
    def task_repo(self) -> BaseRepository[...]: ...

    @abstractmethod
    def task_sequence_repo(self) -> BaseRepository[...]: ...

    @abstractmethod
    def task_tag_repo(self) -> BaseRepository[...]: ...

    @abstractmethod
    def user_repo(self) -> BaseRepository[...]: ...
