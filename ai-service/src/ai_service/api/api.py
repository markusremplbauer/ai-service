from fastapi import APIRouter

from ai_service.api.endpoints import ai_ressource
from ai_service.core.config import settings

api_router = APIRouter(prefix=settings.API_ROOT)
api_router.include_router(ai_ressource.router, prefix="/ai", tags=["ai"])
