from uuid import UUID

from fastapi import APIRouter, Depends, status

from src.core.dependencies import get_service_manager
from src.services import Service

router = APIRouter(prefix="/statuses")


@router.patch(
    "/{status_id}",
    summary="Обновить статус",
    description="Обновляет данные статуса по указанному идентификатору. Возвращает обновлённый объект.",
)
async def update_status(
    status_id: UUID, data: dict, service_manager: Service = Depends(get_service_manager)
):
    return await service_manager.status_service().update(status_id, data)


@router.delete(
    "/{status_id}",
    summary="Удалить статус",
    description="Удаляет статус по указанному идентификатору. При наличии связанных задач возвращает ошибку 400 или 409. При успешном выполнении возвращает статус 204.",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_status(status_id: UUID, service_manager: Service = Depends(get_service_manager)):
    # TODO: проверить наличие связанных задач и вернуть 409, если они есть
    await service_manager.status_service().delete(status_id)
