from fastapi import APIRouter
from starlette import status

router = APIRouter(prefix="/checklist-items")


@router.get(path="/ping", summary="Ping", status_code=status.HTTP_200_OK)
def ping():
    return {"message": "pong"}
