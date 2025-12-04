from fastapi import APIRouter
from starlette import status

router = APIRouter(prefix="/auth")


from fastapi import APIRouter, Depends, status
from uuid import UUID

from src.services import Service
from src.core.dependencies import get_service_manager

router = APIRouter(prefix="/auth")


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    summary="Зарегистрировать пользователя",
    description="Регистрирует нового пользователя. Возвращает созданный объект.",
)
async def register_user(
    data: dict,
    service_manager: Service = Depends(get_service_manager),
):
    return await service_manager.auth_service().register(data)


@router.post(
    "/login",
    summary="Авторизовать пользователя",
    description="Авторизует пользователя по указанным данным. Возвращает токены доступа.",
)
async def login_user(
    data: dict,
    service_manager: Service = Depends(get_service_manager),
):
    return await service_manager.auth_service().login(data["email"], data["password"])
