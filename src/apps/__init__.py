from fastapi import APIRouter

from .exmpl import hint_router_v1
from .health import health_router_v1
from .metrics import metrics_router_v1

routers: dict[str, APIRouter] = {
    "Hint": hint_router_v1,
    "Health": health_router_v1,
    "Metrics": metrics_router_v1,
}

api_router = APIRouter(prefix="/api/v1")

for tag, router in routers.items():
    api_router.include_router(router, tags=[tag])
