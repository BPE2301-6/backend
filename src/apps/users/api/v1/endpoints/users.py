from uuid import UUID

from fastapi import APIRouter, Depends

from src.core.dependencies import get_service_manager

router = APIRouter(prefix="/users")


@router.get(
    "/me",
    summary="Получить текущего пользователя",
    description="Возвращает информацию о текущем пользователе.",
)
async def get_current_user(service_manager=Depends(get_service_manager)):
    # временная заглушка для текущего пользователя
    cur_id = UUID("00000000-0000-0000-0000-000000000001")
    return await service_manager.user_service().get(cur_id)


@router.patch(
    "/me",
    summary="Обновить текущего пользователя",
    description="Обновляет данные текущего пользователя. Возвращает обновлённый объект.",
)
async def update_current_user(data: dict, service_manager=Depends(get_service_manager)):
    # временная заглушка для текущего пользователя
    cur_id = UUID("00000000-0000-0000-0000-000000000001")
    return await service_manager.user_service().update(cur_id, data)


@router.get(
    "",
    summary="Список пользователей",
    description="Возвращает список пользователей по имени или email.",
)
async def list_users(
    search: str = "", limit: int = 20, offset: int = 0, service_manager=Depends(get_service_manager)
):
    users, total = await service_manager.user_service().get_list(
        search=search, limit=limit, offset=offset
    )
    return {"items": users, "total": total, "limit": limit, "offset": offset}


@router.get(
    "/{user_id}",
    summary="Получить пользователя",
    description="Возвращает данные пользователя по указанному идентификатору.",
)
async def get_user(user_id: UUID, service_manager=Depends(get_service_manager)):
    user = await service_manager.user_service().get(user_id)
    return user
