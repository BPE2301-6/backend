import uuid
from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T")


# noinspection DuplicatedCode
class BaseService[T](ABC):
    @abstractmethod
    async def get(self, item_id: uuid.UUID | tuple[uuid.UUID, uuid.UUID]) -> T | None: ...
    @abstractmethod
    async def create(self, data: dict) -> T: ...
    @abstractmethod
    async def update(self, item_id: uuid.UUID | tuple[uuid.UUID, uuid.UUID], data: dict) -> T: ...
    @abstractmethod
    async def delete(self, item_id: uuid.UUID | tuple[uuid.UUID, uuid.UUID]) -> None: ...
    @abstractmethod
    async def get_all(self) -> list[T]: ...


class Service(ABC):
    checklist_items: BaseService[...]
    checklists: BaseService[...]
    comments: BaseService[...]
    project_members: BaseService[...]
    projects: BaseService[...]
    statuses: BaseService[...]
    tags: BaseService[...]
    tasks: BaseService[...]
    task_sequences: BaseService[...]
    task_tags: BaseService[...]
    users: BaseService[...]

    @abstractmethod
    def checklist_item_service(self) -> BaseService[...]: ...
    @abstractmethod
    def checklist_service(self) -> BaseService[...]: ...
    @abstractmethod
    def comment_service(self) -> BaseService[...]: ...
    @abstractmethod
    def project_member_service(self) -> BaseService[...]: ...
    @abstractmethod
    def project_service(self) -> BaseService[...]: ...
    @abstractmethod
    def status_service(self) -> BaseService[...]: ...
    @abstractmethod
    def tag_service(self) -> BaseService[...]: ...
    @abstractmethod
    def task_service(self) -> BaseService[...]: ...
    @abstractmethod
    def task_sequence_service(self) -> BaseService[...]: ...
    @abstractmethod
    def task_tag_service(self) -> BaseService[...]: ...
    @abstractmethod
    def user_service(self) -> BaseService[...]: ...
