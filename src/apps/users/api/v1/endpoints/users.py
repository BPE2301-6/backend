from uuid import UUID

from fastapi import APIRouter, Depends, Query

from src.core.dependencies import get_current_user_id, get_service_manager
from src.core.utils import map_model
from src.services import Service
from src.schemas.pydantic import UserUpdateRequest, UserResponse, UserListResponse

router = APIRouter(prefix="/users")


@router.get(
    "/me",
    summary="Получить текущего пользователя",
    description="Возвращает информацию о текущем пользователе.",
)
async def get_current_user(
    user_id: UUID = Depends(get_current_user_id),
    service_manager: Service = Depends(get_service_manager),
) -> UserResponse:
    return await service_manager.user_service().get(user_id)


@router.patch(
    "/me",
    summary="Обновить текущего пользователя",
    description="Обновляет данные текущего пользователя. Возвращает обновлённый объект.",
)
async def update_current_user(
    data: UserUpdateRequest,
    user_id: UUID = Depends(get_current_user_id),
    service_manager: Service = Depends(get_service_manager),
) -> UserResponse:
    return await service_manager.user_service().update(user_id, data.model_dump(exclude_unset=True))


@router.get(
    "",
    summary="Список пользователей",
    description="Возвращает список пользователей по имени или email.",
)
async def list_users(
    search: str = Query("", description="Фильтр по имени или email"),
    limit: int = Query(20, ge=1),
    offset: int = Query(0, ge=0),
    service_manager: Service = Depends(get_service_manager),
) -> UserListResponse:
    items, total = await service_manager.user_service().get_list(
        search=search, limit=limit, offset=offset
    )
    return UserListResponse(
        items=[map_model(item, UserResponse) for item in items],
        total=total,
        limit=limit,
        offset=offset,
    )


@router.get(
    "/{user_id}",
    summary="Получить пользователя",
    description="Возвращает данные пользователя по указанному идентификатору.",
)
async def get_user(
    user_id: UUID,
    service_manager: Service = Depends(get_service_manager),
) -> UserResponse:
    return await service_manager.user_service().get(user_id)
