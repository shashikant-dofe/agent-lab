from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.core.config import settings
from app.api.routes.conversation import (
    router as conversation_router,
)
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(health_router)
app.include_router(conversation_router)

@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.app_name} 🚀"
    }