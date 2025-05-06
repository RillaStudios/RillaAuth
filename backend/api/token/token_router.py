from datetime import timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from app.config import settings
from app.db.auth_db.auth_db import AuthDbSession
from app.db.auth_db.models.token import Token
from service.user.user_service import authenticate_user
from service.token.token_service import create_access_token

token_router = APIRouter()

@token_router.post("/token")  # Note: Should be POST, not GET for login
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: AuthDbSession
) -> Token:
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")