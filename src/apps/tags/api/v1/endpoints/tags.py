from fastapi import APIRouter, Depends, status
from uuid import UUID

from src.services import Service
from src.core.dependencies import get_service_manager

router = APIRouter(prefix="/tags")


@router.patch(
    "/{tag_id}",
    summary="Обновить тег",
    description="Обновляет данные тега по указанному идентификатору. Возвращает обновлённый объект.",
)
async def update_tag(
    tag_id: UUID,
    data: dict,
    service_manager: Service = Depends(get_service_manager),
):
    return await service_manager.tag_service().update(tag_id, data)


@router.delete(
    "/{tag_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить тег",
    description="Удаляет тег по указанному идентификатору. При успешном выполнении возвращает статус 204.",
)
async def delete_tag(
    tag_id: UUID,
    service_manager: Service = Depends(get_service_manager),
):
    await service_manager.tag_service().delete(tag_id)
