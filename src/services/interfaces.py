import uuid
from abc import ABC, abstractmethod
from typing import Any, TypeVar

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
    auth: BaseService[Any]
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

    @abstractmethod
    def auth_service(self) -> BaseService[Any]: ...

    @abstractmethod
    def checklist_item_service(self) -> BaseService[Any]: ...

    @abstractmethod
    def checklist_service(self) -> BaseService[Any]: ...

    @abstractmethod
    def comment_service(self) -> BaseService[Any]: ...

    @abstractmethod
    def project_member_service(self) -> BaseService[Any]: ...

    @abstractmethod
    def project_service(self) -> BaseService[Any]: ...

    @abstractmethod
    def status_service(self) -> BaseService[Any]: ...

    @abstractmethod
    def tag_service(self) -> BaseService[Any]: ...

    @abstractmethod
    def task_service(self) -> BaseService[Any]: ...

    @abstractmethod
    def task_sequence_service(self) -> BaseService[Any]: ...

    @abstractmethod
    def task_tag_service(self) -> BaseService[Any]: ...

    @abstractmethod
    def user_service(self) -> BaseService[Any]: ...
