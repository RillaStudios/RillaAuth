from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.auth.auth_router import auth_router
from api.token.token_router import token_router
from api.user.user_router import user_router
from core.config import settings
from db.db import init_db

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    root_path="/auth",
)

app.include_router(auth_router)
app.include_router(token_router, prefix="/token")
app.include_router(user_router, prefix="/users")

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

init_db()