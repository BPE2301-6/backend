from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.lifespan import lifespan
from src.apps import api_router  # основной router
from src.config import cfg
from src.core import MetricsMiddleware

# from src.core.middleware import setup_middlewares
# from src.core.exceptions import setup_exception_handlers

app = FastAPI(title="My FastAPI App", version="1.0.0", lifespan=lifespan)
# Include middlewares
app.add_middleware(MetricsMiddleware)
# Register API
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=cfg.docs.allowed_ips,
    allow_credentials=True,
    allow_methods=["*"],
)

# Опционально: Middleware, Exceptions
# setup_middlewares(app)
# setup_exception_handlers(app)


def main():
    import uvicorn

    uvicorn.run(
        app="src.api.main:app",
        host=cfg.app.host,
        port=cfg.app.port,
        reload=cfg.app.reload,
        workers=cfg.app.workers,
    )
