from fastapi import HTTPException
from starlette import status

disabled_user_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Inactive user",
    headers={"WWW-Authenticate": "Bearer"},
)