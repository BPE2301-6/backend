from uuid import UUID

from fastapi import APIRouter, Depends
from starlette import status

from src.core.dependencies import get_service_manager
from src.core.utils import map_model
from src.schemas.pydantic import ChecklistItemCreateRequest, ChecklistItemResponse
from src.services import Service

router = APIRouter(prefix="/checklists")


@router.delete(
    "/{checklist_id}",
    summary="Удалить чеклист",
    description=(
        "Удаляет чеклист по указанному идентификатору. "
        "При успешном выполнении возвращает статус 204."
    ),
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_checklist(
    checklist_id: UUID, service_manager: Service = Depends(get_service_manager)
):
    await service_manager.checklist_service().delete(checklist_id)


@router.get(
    "/{checklist_id}/items",
    summary="Получить элементы чеклиста",
    status_code=status.HTTP_200_OK,
)
async def get_checklist_items(
    checklist_id: UUID,
    service_manager: Service = Depends(get_service_manager),
) -> list[ChecklistItemResponse]:
    dtos = await service_manager.checklist_item_service().get_by_checklist_id(checklist_id)
    return [map_model(dto, ChecklistItemResponse) for dto in dtos]



@router.post(
    "/{checklist_id}/items",
    summary="Добавить элемент в чеклист",
    status_code=status.HTTP_201_CREATED,
)
async def create_checklist_item(
    checklist_id: UUID,
    data: ChecklistItemCreateRequest,
    service_manager: Service = Depends(get_service_manager),
) -> ChecklistItemResponse:
    payload = data.model_dump(exclude_unset=True)
    payload["checklist_id"] = checklist_id
    dto = await service_manager.checklist_item_service().create(payload)
    return map_model(dto, ChecklistItemResponse)
