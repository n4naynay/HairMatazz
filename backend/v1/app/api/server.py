from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from backend.v1.app.api import router
from backend.v1.app.core.settings_factory import get_settings


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router, prefix=settings.API_PREFIX)

    return app


app = create_app()

