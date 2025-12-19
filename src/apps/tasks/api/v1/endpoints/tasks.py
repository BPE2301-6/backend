from uuid import UUID

from fastapi import APIRouter, Depends, Query, status

from src.core.dependencies import get_current_user_id, get_service_manager
from src.core.utils import map_model
from src.schemas.pydantic import (
    ChecklistResponse,
    CommentListResponse,
    CommentRequest,
    CommentResponse,
    TaskMoveRequest,
    TaskResponse,
    TaskTagRequest,
    TaskTagResponse,
    TaskUpdateRequest,
)
from src.services import Service

router = APIRouter(prefix="/tasks")


@router.get(
    "/{task_id}",
    summary="Получить задачу",
    description="Возвращает данные задачи по указанному идентификатору.",
)
async def get_task(
    task_id: UUID, service_manager: Service = Depends(get_service_manager)
) -> TaskResponse:
    dto = await service_manager.task_service().get(task_id)
    return map_model(dto, TaskResponse)


@router.patch(
    "/{task_id}",
    summary="Обновить задачу",
    description=(
        "Обновляет данные задачи по указанному идентификатору. " "Возвращает обновлённый объект."
    ),
)
async def update_task(
    task_id: UUID, data: TaskUpdateRequest, service_manager: Service = Depends(get_service_manager)
) -> TaskResponse:
    dto = await service_manager.task_service().update(task_id, data.model_dump(exclude_unset=True))
    return map_model(dto, TaskResponse)


@router.post(
    "/{task_id}/move",
    summary="Переместить задачу",
    description=(
        "Переводит задачу в другой статус по указанному идентификатору. "
        "Возвращает обновлённый объект."
    ),
)
async def move_task(
    task_id: UUID, data: TaskMoveRequest, service_manager: Service = Depends(get_service_manager)
) -> TaskResponse:
    dto = await service_manager.task_service().update(task_id, data.model_dump(exclude_unset=True))
    return map_model(dto, TaskResponse)


@router.delete(
    "/{task_id}",
    summary="Удалить задачу",
    description=(
        "Удаляет задачу по указанному идентификатору. "
        "При успешном выполнении возвращает статус 204."
    ),
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_task(task_id: UUID, service_manager: Service = Depends(get_service_manager)):
    await service_manager.task_service().delete(task_id)


@router.post(
    "/{task_id}/tags",
    summary="Привязать теги к задаче",
    description=(
        "Привязывает один или несколько тегов к задаче по указанным идентификаторам. "
        "Возвращает список идентификаторов привязанных тегов."
    ),
    status_code=status.HTTP_201_CREATED,
)
async def attach_tags(
    task_id: UUID, data: TaskTagRequest, service_manager: Service = Depends(get_service_manager)
) -> TaskTagResponse:
    tag_ids = await service_manager.task_tag_service().attach_tags(task_id, data.tag_ids)
    return TaskTagResponse(tag_ids=tag_ids)


@router.delete(
    "/{task_id}/tags/{tag_id}",
    summary="Отвязать тег от задачи",
    description=(
        "Удаляет привязку тега от задачи по идентификатору. "
        "При успешном выполнении возвращает статус 204."
    ),
    status_code=status.HTTP_204_NO_CONTENT,
)
async def detach_tag(
    task_id: UUID, tag_id: UUID, service_manager: Service = Depends(get_service_manager)
):
    await service_manager.task_tag_service().delete((task_id, tag_id))


@router.get(
    "/{task_id}/comments",
    summary="Получить комментарии задачи",
    description=(
        "Возвращает список комментариев задачи, "
        "отсортированных по времени создания (по возрастанию)."
    ),
    status_code=status.HTTP_200_OK,
)
async def list_comments(
    task_id: UUID,
    limit: int = Query(20, ge=1),
    offset: int = Query(0, ge=0),
    service_manager: Service = Depends(get_service_manager),
) -> CommentListResponse:
    items, total = await service_manager.comment_service().get_all_by_task(
        task_id, limit=limit, offset=offset
    )
    return CommentListResponse(
        items=[map_model(item, CommentResponse) for item in items],
        total=total,
        limit=limit,
        offset=offset,
    )


@router.post(
    "/{task_id}/comments",
    summary="Создать комментарий задачи",
    description="Создаёт новый комментарий по идентификатору задачи. Возвращает созданный объект.",
    status_code=status.HTTP_201_CREATED,
)
async def create_comment(
    task_id: UUID,
    data: CommentRequest,
    user_id: UUID = Depends(get_current_user_id),
    service_manager: Service = Depends(get_service_manager),
) -> CommentResponse:
    payload = data.model_dump(exclude_unset=True)
    payload["task_id"] = task_id
    payload["author_id"] = user_id
    dto = await service_manager.comment_service().create(payload)
    return map_model(dto, CommentResponse)


@router.get(
    "/{task_id}/checklists",
    summary="Получить чеклисты задачи",
    description="Возвращает список чеклистов по идентификатору задачи.",
    status_code=status.HTTP_200_OK,
)
async def get_checklists(
    task_id: UUID, service_manager: Service = Depends(get_service_manager)
) -> list[ChecklistResponse]:
    checklist = await service_manager.checklist_service().get_by_task_id(task_id)
    return [map_model(checklist, ChecklistResponse)] if checklist else []


@router.post(
    "/{task_id}/checklists",
    summary="Создать чеклист задачи",
    description="Создаёт новый чеклист по идентификатору задачи. Возвращает созданный объект.",
    status_code=status.HTTP_201_CREATED,
)
async def create_checklist(
    task_id: UUID, service_manager: Service = Depends(get_service_manager)
) -> ChecklistResponse:
    data = {"task_id": task_id}
    dto = await service_manager.checklist_service().create(data)
    return map_model(dto, ChecklistResponse)
