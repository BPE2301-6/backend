from uuid import UUID

from fastapi import APIRouter, Depends, status

from src.core.dependencies import get_service_manager
from src.services import Service

router = APIRouter(prefix="/checklist-items")


@router.patch(
    "/{item_id}",
    summary="Обновить элемент чеклиста",
    description=(
        "Обновляет данные элемента чеклиста по указанному идентификатору. "
        "Возвращает обновлённый объект."
    ),
)
async def update_checklist_item(
    item_id: UUID, data: dict, service_manager: Service = Depends(get_service_manager)
):
    return await service_manager.checklist_item_service().update(item_id, data)


@router.delete(
    "/{item_id}",
    summary="Удалить элемент чеклиста",
    description=(
        "Удаляет элемент чеклиста по указанному идентификатору. "
        "При успешном выполнении возвращает статус 204."
    ),
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_checklist_item(
    item_id: UUID, service_manager: Service = Depends(get_service_manager)
):
    await service_manager.checklist_item_service().delete(item_id)
