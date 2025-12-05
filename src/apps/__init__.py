from fastapi import APIRouter

from .auth import auth_router_v1
from .checklist_items import checklist_items_router_v1
from .checklists import checklists_router_v1
from .comments import comments_router_v1
from .health import health_router_v1
from .metrics import metrics_router_v1
from .projects import projects_router_v1
from .search import search_router_v1
from .statuses import statuses_router_v1
from .tags import tags_router_v1
from .tasks import tasks_router_v1
from .users import users_router_v1

routers: dict[str, APIRouter] = {
    "Auth": auth_router_v1,
    "Checklist items": checklist_items_router_v1,
    "Checklists": checklists_router_v1,
    "Comments": comments_router_v1,
    "Health": health_router_v1,
    "Metrics": metrics_router_v1,
    "Projects": projects_router_v1,
    "Search": search_router_v1,
    "Statuses": statuses_router_v1,
    "Tags": tags_router_v1,
    "Tasks": tasks_router_v1,
    "Users": users_router_v1,
}

api_router = APIRouter(prefix="/api/v1")

for tag, router in routers.items():
    api_router.include_router(router, tags=[tag])
