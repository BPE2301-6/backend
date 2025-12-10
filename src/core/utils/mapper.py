from __future__ import annotations

from dataclasses import asdict, is_dataclass
from typing import Any, TypeVar

from pydantic import BaseModel

T = TypeVar("T")
U = TypeVar("U")


def map_model(source: Any, target_type: type[U]) -> U:
    if source is None:
        raise ValueError("Source cannot be None")

    if isinstance(source, BaseModel):
        data = source.model_dump(exclude_unset=True)
    elif is_dataclass(source):
        data = asdict(source)
    elif hasattr(source, "__dict__"):
        data = dict(vars(source))
    elif isinstance(source, dict):
        data = source
    else:
        raise TypeError(f"Unsupported source type: {type(source)}")

    target_fields = {f for f in getattr(target_type, "__annotations__", {})}
    filtered_data = {k: v for k, v in data.items() if k in target_fields}

    return target_type(**filtered_data)
