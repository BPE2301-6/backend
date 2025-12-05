from fastapi import APIRouter, Depends
from starlette import status
from uuid import UUID

from src.services import Service
from src.core.dependencies import get_service_manager

router = APIRouter(prefix="/comments")


@router.delete(
    path="/{comment_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить комментарий",
    description="Удаляет комментарий по указанному идентификатору. При успешном выполнении возвращает статус 204.",
)
async def delete_comment(
    comment_id: UUID,
    service_manager: Service = Depends(get_service_manager),
):
    await service_manager.comment_service().delete(comment_id)
