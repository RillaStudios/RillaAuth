from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.app.service_router import service_router
from api.auth.auth_router import auth_router
from api.db.db_router import db_router
from api.themes.themes_router import themes_router
from api.token.token_router import token_router
from api.user.user_router import user_router
from app.config import settings
from app.lifecycle.app_lifecycle import lifespan

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    root_path="/auth",
    lifespan=lifespan,
)

app.include_router(service_router, prefix="/service")
app.include_router(auth_router, prefix="/auth")
app.include_router(db_router, prefix="/db")
app.include_router(token_router, prefix="/token")
app.include_router(user_router, prefix="/users")
app.include_router(themes_router, prefix="/theme")

# CORS (adjust origins in prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
    expose_headers=settings.CORS_EXPOSE_HEADERS,
    max_age=settings.CORS_MAX_AGE,
)