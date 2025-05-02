# Exception to be raised if credentials are invalid
from fastapi import HTTPException
from starlette import status

# Exception to be raised if credentials are invalid
credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

# Exception to be raised if token is expired
expired_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token has expired",
    headers={"WWW-Authenticate": "Bearer"},
)

# Exception to be raised if token is malformed
malformed_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Malformed token",
    headers={"WWW-Authenticate": "Bearer"},
)

# Exception to be raised if token is not found
not_found_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token not found",
    headers={"WWW-Authenticate": "Bearer"},
)

