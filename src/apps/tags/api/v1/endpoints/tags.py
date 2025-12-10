from uuid import UUID

from fastapi import APIRouter, Depends, status

from src.core.dependencies import get_service_manager
from src.services import Service
from src.schemas.pydantic import TagUpdateRequest, TagResponse

router = APIRouter(prefix="/tags")


@router.patch(
    "/{tag_id}",
    summary="Обновить тег",
    description=(
        "Обновляет данные тега по указанному идентификатору. "
        "Возвращает обновлённый объект."
    ),
)
async def update_tag(
    tag_id: UUID,
    data: TagUpdateRequest,
    service_manager: Service = Depends(get_service_manager),
) -> TagResponse:
    return await service_manager.tag_service().update(tag_id, data.model_dump(exclude_unset=True))


@router.delete(
    "/{tag_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить тег",
    description=(
        "Удаляет тег по указанному идентификатору. "
        "При успешном выполнении возвращает статус 204."
    ),
)
async def delete_tag(
    tag_id: UUID,
    service_manager: Service = Depends(get_service_manager),
):
    await service_manager.tag_service().delete(tag_id)
