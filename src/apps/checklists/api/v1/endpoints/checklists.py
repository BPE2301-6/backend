from uuid import UUID

from fastapi import APIRouter, Depends
from starlette import status

from src.core.dependencies import get_service_manager
from src.services import Service

router = APIRouter(prefix="/checklists")


@router.get(
    "/tasks/{task_id}/checklists",
    summary="Получить чеклист",
    description=(
        "Возвращает чеклист по идентификатору задачи. "
        "При отсутствии чеклиста возвращает пустой список."
    ),
    status_code=status.HTTP_200_OK,
)
async def get_checklists(task_id: UUID, service_manager: Service = Depends(get_service_manager)):
    checklist = await service_manager.checklist_service().get_by_task_id(task_id)
    return [checklist] if checklist else []


@router.post(
    "/tasks/{task_id}/checklists",
    summary="Создать чеклист",
    description=("Создаёт новый чеклист по идентификатору задачи. " "Возвращает созданный объект."),
    status_code=status.HTTP_201_CREATED,
)
async def create_checklist(task_id: UUID, service_manager: Service = Depends(get_service_manager)):
    data = {"task_id": task_id}
    return await service_manager.checklist_service().create(data)


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
