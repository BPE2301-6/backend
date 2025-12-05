from uuid import UUID

from fastapi import APIRouter, Depends, Query, status

from src.core.dependencies import get_service_manager

router = APIRouter(prefix="/projects")


@router.post(
    path="",
    status_code=status.HTTP_201_CREATED,
    summary="Создать проект",
    description=("Создаёт новый проект. Возвращает созданный объект."),
)
async def create_project(data: dict, service_manager=Depends(get_service_manager)):
    return await service_manager.project_service().create(data)


@router.get(
    path="",
    summary="Получить список проектов",
    description=(
        "Возвращает список проектов. Поддерживает поиск " "по имени и ключу, а также пагинацию."
    ),
)
async def list_projects(
    search: str | None = None,
    limit: int = 20,
    offset: int = 0,
    service_manager=Depends(get_service_manager),
):
    return await service_manager.project_service().get_list(
        search=search, limit=limit, offset=offset
    )


@router.get(
    path="/{project_id}",
    summary="Получить проект",
    description="Возвращает данные проекта по указанному идентификатору.",
)
async def get_project(project_id: UUID, service_manager=Depends(get_service_manager)):
    return await service_manager.project_service().get(project_id)


@router.patch(
    path="/{project_id}",
    summary="Обновить проект",
    description=(
        "Обновляет данные проекта по указанному идентификатору. " "Возвращает обновлённый объект."
    ),
)
async def update_project(
    project_id: UUID, data: dict, service_manager=Depends(get_service_manager)
):
    return await service_manager.project_service().update(project_id, data)


@router.delete(
    path="/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить проект",
    description=(
        "Удаляет проект по указанному идентификатору. "
        "При успешном выполнении возвращает статус 204."
    ),
)
async def delete_project(project_id: UUID, service_manager=Depends(get_service_manager)):
    await service_manager.project_service().delete(project_id)


@router.get(
    "/{project_id}/members",
    summary="Получить участников проекта",
    description="Возвращает список участников проекта.",
    status_code=status.HTTP_200_OK,
)
async def get_project_members(project_id: UUID, service_manager=Depends(get_service_manager)):
    return await service_manager.project_member_service().get_all_by_project(project_id)


@router.post(
    "/{project_id}/members",
    summary="Добавить участника проекта",
    description="Добавляет нового участника в проект. Возвращает созданный объект.",
    status_code=status.HTTP_201_CREATED,
)
async def add_project_member(
    project_id: UUID, data: dict, service_manager=Depends(get_service_manager)
):
    data["project_id"] = project_id
    return await service_manager.project_member_service().create(data)


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
    project_id: UUID, user_id: UUID, data: dict, service_manager=Depends(get_service_manager)
):
    # TODO: Проверить, что хотя бы один OWNER остаётся
    item_id: tuple[UUID, UUID] = (project_id, user_id)
    return await service_manager.project_member_service().update(item_id, data)


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
    project_id: UUID, user_id: UUID, service_manager=Depends(get_service_manager)
):
    # TODO: Проверить, что хотя бы один OWNER остаётся
    item_id: tuple[UUID, UUID] = (project_id, user_id)
    await service_manager.project_member_service().delete(item_id)


@router.get(
    "/{project_id}/statuses",
    summary="Получить статусы проекта",
    description="Возвращает список статусов проекта.",
    status_code=status.HTTP_200_OK,
)
async def get_project_statuses(project_id: UUID, service_manager=Depends(get_service_manager)):
    return await service_manager.status_service().get_all_by_project(project_id)


@router.post(
    "/{project_id}/statuses",
    summary="Создать статус проекта",
    description="Создаёт новый статус по идентификатору проекта. Возвращает созданный объект.",
    status_code=status.HTTP_201_CREATED,
)
async def create_project_status(
    project_id: UUID, data: dict, service_manager=Depends(get_service_manager)
):
    data["project_id"] = project_id
    return await service_manager.status_service().create(data)


@router.post(
    "/{project_id}/tasks",
    summary="Создать задачу проекта",
    description="Создаёт новую задачу по идентификатору проекта. Возвращает созданный объект.",
    status_code=status.HTTP_201_CREATED,
)
async def create_project_task(
    project_id: UUID, data: dict, service_manager=Depends(get_service_manager)
):
    data["project_id"] = project_id
    return await service_manager.task_service().create(data)


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
    service_manager=Depends(get_service_manager),
):
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
    return {"items": items, "total": total, "limit": limit, "offset": offset}


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
    service_manager=Depends(get_service_manager),
):
    items, total = await service_manager.tag_service().get_all_by_project(project_id, limit, offset)
    return {"items": items, "total": total, "limit": limit, "offset": offset}


@router.post(
    "/{project_id}/tags",
    summary="Создать тег проекта",
    description="Создаёт новый тег по идентификатору проекта. Возвращает созданный объект.",
    status_code=status.HTTP_201_CREATED,
)
async def create_project_tag(
    project_id: UUID, data: dict, service_manager=Depends(get_service_manager)
):
    data["project_id"] = project_id
    return await service_manager.tag_service().create(data)
