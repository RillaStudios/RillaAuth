from typing import Annotated
import jwt
from fastapi import HTTPException, Depends
from jwt import InvalidTokenError
from sqlmodel import Session, select
from starlette import status
from core.config import settings
from db.db import SessionDep
from db.models.token import TokenData
from db.models.user import User
from service.auth.password_crypt import verify_password
from service.token.token_exceptions import credentials_exception, malformed_exception


def get_user(db: Session, username: str) -> User | None:
    statement = select(User).where(User.username == username)
    return db.exec(statement).first()

def authenticate_user(db: Session, username: str, password: str) -> User | bool:
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):  # Use `user.password`
        return False
    return user

async def get_current_user(token: Annotated[str, Depends(settings.AUTH_SCHEME)],
                           db: SessionDep) -> User:
    """
    Get the current user from the token.

    This function decodes the JWT token and retrieves the user
    information from the database. If the token is invalid or
    the user is not found, an HTTPException is raised.

    :param token: JWT token to decode.
    :param db: Database session dependency.
    :return:

    @author IFD
    @date 2025-05-01
    """

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        username = payload.get("sub")

        if username is None:
            raise credentials_exception

        token_data = TokenData(username=username)

    except InvalidTokenError:
        raise malformed_exception

    user = get_user(db, username=token_data.username)

    if user is None:
        raise credentials_exception

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user