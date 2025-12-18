from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class Paginated(BaseModel, Generic[T]): # noqa: UP046
    items: list[T]
    total: int
    limit: int
    offset: int
