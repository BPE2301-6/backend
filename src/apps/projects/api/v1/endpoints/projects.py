from uuid import UUID

from fastapi import APIRouter, Depends, Query, status

from src.core.dependencies import get_service_manager
from src.core.utils import map_model
from src.schemas.pydantic import (
    ProjectCreateRequest,
    ProjectListResponse,
    ProjectMemberCreateRequest,
    ProjectMemberResponse,
    ProjectMemberUpdateRequest,
    ProjectResponse,
    ProjectUpdateRequest,
    StatusCreateRequest,
    StatusResponse,
    TagCreateRequest,
    TagListItem,
    TagListResponse,
    TagResponse,
    TaskCreateRequest,
    TaskListResponse,
    TaskResponse,
)
from src.services import Service

router = APIRouter(prefix="/projects")


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Создать проект",
    description="Создаёт новый проект. Возвращает созданный объект.",
)
async def create_project(
    data: ProjectCreateRequest, service_manager: Service = Depends(get_service_manager)
) -> ProjectResponse:
    dto = await service_manager.project_service().create(data.model_dump(exclude_unset=True))
    return map_model(dto, ProjectResponse)


@router.get(
    "",
    summary="Получить список проектов",
    description=(
        "Возвращает список проектов. "
        "Поддерживает поиск по имени и ключу, а также пагинацию."
    ),
)
async def list_projects(
    search: str | None = Query(default=None),
    limit: int = Query(default=20, ge=1),
    offset: int = Query(default=0, ge=0),
    service_manager: Service = Depends(get_service_manager),
) -> ProjectListResponse:
    items, total = await service_manager.project_service().get_list(
        search=search, limit=limit, offset=offset
    )
    return ProjectListResponse(
        items=[map_model(item, ProjectResponse) for item in items],
        total=total,
        limit=limit,
        offset=offset,
    )


@router.get(
    "/{project_id}",
    summary="Получить проект",
    description="Возвращает данные проекта по указанному идентификатору.",
)
async def get_project(
    project_id: UUID, service_manager: Service = Depends(get_service_manager)
) -> ProjectResponse:
    dto = await service_manager.project_service().get(project_id)
    return map_model(dto, ProjectResponse)


@router.patch(
    "/{project_id}",
    summary="Обновить проект",
    description=(
        "Обновляет данные проекта по указанному идентификатору. "
        "Возвращает обновлённый объект."
    ),
)
async def update_project(
    project_id: UUID,
    data: ProjectUpdateRequest,
    service_manager: Service = Depends(get_service_manager),
) -> ProjectResponse:
    dto = await service_manager.project_service().update(
        project_id, data.model_dump(exclude_unset=True)
    )
    return map_model(dto, ProjectResponse)


@router.delete(
    "/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить проект",
    description=(
        "Удаляет проект по указанному идентификатору. "
        "При успешном выполнении возвращает статус 204."
    ),
)
async def delete_project(project_id: UUID, service_manager: Service = Depends(get_service_manager)):
    await service_manager.project_service().delete(project_id)


@router.get(
    "/{project_id}/members",
    summary="Получить участников проекта",
    description="Возвращает список участников проекта.",
    status_code=status.HTTP_200_OK,
)
async def get_project_members(
    project_id: UUID, service_manager: Service = Depends(get_service_manager)
) -> list[ProjectMemberResponse]:
    dtos = await service_manager.project_member_service().get_all_by_project(project_id)
    return [map_model(dto, ProjectMemberResponse) for dto in dtos]


@router.post(
    "/{project_id}/members",
    summary="Добавить участника проекта",
    description="Добавляет нового участника в проект. Возвращает созданный объект.",
    status_code=status.HTTP_201_CREATED,
)
async def add_project_member(
    project_id: UUID,
    data: ProjectMemberCreateRequest,
    service_manager: Service = Depends(get_service_manager),
) -> ProjectMemberResponse:
    payload = data.model_dump(exclude_unset=True)
    payload["project_id"] = project_id
    dto = await service_manager.project_member_service().create(payload)
    return map_model(dto, ProjectMemberResponse)


@router.patch(
    "/{project_id}/members/{user_id}",
    summary="Обновить роль участника",
    description=(
        "Обновляет роль участника проекта по указанному идентификатору. "
        "Возвращает обновлённый объект."
    ),
    status_code=status.HTTP_200_OK,
)
async def update_project_member(
    project_id: UUID,
    user_id: UUID,
    data: ProjectMemberUpdateRequest,
    service_manager: Service = Depends(get_service_manager),
) -> ProjectMemberResponse:
    item_id: tuple[UUID, UUID] = (project_id, user_id)
    dto = await service_manager.project_member_service().update(
        item_id, data.model_dump(exclude_unset=True)
    )
    return map_model(dto, ProjectMemberResponse)


@router.delete(
    "/{project_id}/members/{user_id}",
    summary="Удалить участника проекта",
    description=(
        "Удаляет участника проекта по указанному идентификатору. "
        "При успешном выполнении возвращает статус 204."
    ),
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_project_member(
    project_id: UUID, user_id: UUID, service_manager: Service = Depends(get_service_manager)
):
    item_id: tuple[UUID, UUID] = (project_id, user_id)
    await service_manager.project_member_service().delete(item_id)


@router.get(
    "/{project_id}/statuses",
    summary="Получить статусы проекта",
    description="Возвращает список статусов проекта.",
    status_code=status.HTTP_200_OK,
)
async def get_project_statuses(
    project_id: UUID, service_manager: Service = Depends(get_service_manager)
) -> list[StatusResponse]:
    dtos = await service_manager.status_service().get_all_by_project(project_id)
    return [map_model(dto, StatusResponse) for dto in dtos]


@router.post(
    "/{project_id}/statuses",
    summary="Создать статус проекта",
    description="Создаёт новый статус по идентификатору проекта. Возвращает созданный объект.",
    status_code=status.HTTP_201_CREATED,
)
async def create_project_status(
    project_id: UUID,
    data: StatusCreateRequest,
    service_manager: Service = Depends(get_service_manager),
) -> StatusResponse:
    payload = data.model_dump(exclude_unset=True)
    payload["project_id"] = project_id
    dto = await service_manager.status_service().create(payload)
    return map_model(dto, StatusResponse)


@router.post(
    "/{project_id}/tasks",
    summary="Создать задачу проекта",
    description="Создаёт новую задачу по идентификатору проекта. Возвращает созданный объект.",
    status_code=status.HTTP_201_CREATED,
)
async def create_project_task(
    project_id: UUID,
    data: TaskCreateRequest,
    service_manager: Service = Depends(get_service_manager),
) -> TaskResponse:
    payload = data.model_dump(exclude_unset=True)
    payload["project_id"] = project_id
    dto = await service_manager.task_service().create(payload)
    return map_model(dto, TaskResponse)


@router.get(
    "/{project_id}/tasks",
    summary="Получить задачи проекта",
    description="Возвращает список задач проекта с фильтрацией, пагинацией и сортировкой.",
    status_code=status.HTTP_200_OK,
)
async def list_project_tasks(
    project_id: UUID,
    status_id: UUID | None = None,
    assignee_id: UUID | None = None,
    reporter_id: UUID | None = None,
    priority: str | None = None,
    tag_id: UUID | None = None,
    q: str | None = None,
    due_from: str | None = None,
    due_to: str | None = None,
    limit: int = Query(20, ge=1),
    offset: int = Query(0, ge=0),
    sort: str = Query("-created_at"),
    service_manager: Service = Depends(get_service_manager),
) -> TaskListResponse:
    filters = {
        k: v
        for k, v in {
            "status_id": status_id,
            "assignee_id": assignee_id,
            "reporter_id": reporter_id,
            "priority": priority,
            "tag_id": tag_id,
            "q": q,
            "due_from": due_from,
            "due_to": due_to,
        }.items()
        if v is not None
    }

    items, total = await service_manager.task_service().get_all_by_project(
        project_id, filters, limit, offset, sort
    )
    return TaskListResponse(
        items=[map_model(item, TaskResponse) for item in items],
        total=total,
        limit=limit,
        offset=offset,
    )


@router.get(
    "/{project_id}/tags",
    summary="Получить теги проекта",
    description="Возвращает список тегов по идентификатору проекта.",
    status_code=status.HTTP_200_OK,
)
async def list_project_tags(
    project_id: UUID,
    limit: int = Query(50, ge=1),
    offset: int = Query(0, ge=0),
    service_manager: Service = Depends(get_service_manager),
) -> TagListResponse:
    items, total = await service_manager.tag_service().get_all_by_project(project_id, limit, offset)
    return TagListResponse(
        items=[map_model(item, TagListItem) for item in items],
        total=total,
        limit=limit,
        offset=offset,
    )


@router.post(
    "/{project_id}/tags",
    summary="Создать тег проекта",
    description="Создаёт новый тег по идентификатору проекта. Возвращает созданный объект.",
    status_code=status.HTTP_201_CREATED,
)
async def create_project_tag(
    project_id: UUID,
    data: TagCreateRequest,
    service_manager: Service = Depends(get_service_manager),
) -> TagResponse:
    payload = data.model_dump(exclude_unset=True)
    payload["project_id"] = project_id
    dto = await service_manager.tag_service().create(payload)
    return map_model(dto, TagResponse)
