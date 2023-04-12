import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ai_service.api.api import api_router
from ai_service.core.config import settings

logging.basicConfig(level=logging.INFO)


def create_app(debug: bool):
    app = FastAPI(
        title="ai_service",
        debug=debug,
        openapi_url=f"{settings.API_ROOT}/openapi.json",
        docs_url=settings.API_ROOT if settings.API_ROOT else "/",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)

    return app


def production_app():
    return create_app(debug=False)


def development_app():
    return create_app(debug=True)


def run_server(debug: bool = False):
    app_name = "production_app" if not debug else "development_app"
    uvicorn.run(
        f"{__name__}:{app_name}",
        factory=True,
        host="0.0.0.0",
        port=settings.API_PORT,
        reload=debug,
    )