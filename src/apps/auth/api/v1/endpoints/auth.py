from fastapi import APIRouter, Depends, status

from src.core.dependencies import get_service_manager
from src.core.utils import map_model
from src.services import Service

from src.schemas.pydantic import (
    AuthRegisterRequest,
    AuthLoginRequest,
    AuthRegisterResponseUser,
    AuthRegisterResponse,
    AuthLoginResponse
)

router = APIRouter(prefix="/auth")


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    summary="Зарегистрировать пользователя",
    description="Регистрирует нового пользователя. Возвращает созданный объект.",
)
async def register_user(
    data: AuthRegisterRequest,
    service_manager: Service = Depends(get_service_manager),
) -> AuthRegisterResponse:
    user_dto = await service_manager.auth_service().register(data.model_dump(exclude_unset=True))
    user_response = map_model(user_dto, AuthRegisterResponseUser)
    return AuthRegisterResponse(user=user_response)


@router.post(
    "/login",
    summary="Авторизовать пользователя",
    description="Авторизует пользователя по указанным данным. Возвращает токены доступа.",
)
async def login_user(
    data: AuthLoginRequest,
    service_manager: Service = Depends(get_service_manager),
) -> AuthLoginResponse:
    return await service_manager.auth_service().login(data.model_dump(exclude_unset=True))
