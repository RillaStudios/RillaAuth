from fastapi import HTTPException
from sqlmodel import select
from starlette import status

from db.db import get_session
from db.models.user import User
from service.auth.password_crypt import pwd_context


async def register_user(user: User) -> User:
    """
    Register a new user in the system.

    Args:
        user (User): The user object containing registration data

    Returns:
        User: The created user object with hashed password

    Raises:
        HTTPException: If username or email already exists
    """
    session = next(get_session())
    try:
        # Check if username already exists
        existing_user = session.exec(
            select(User).where(User.username == user.username)
        ).first()

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered"
            )

        # Check if email already exists
        existing_email = session.exec(
            select(User).where(User.email == user.email)
        ).first()

        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        # Hash the password
        hashed_password = pwd_context.hash(user.password)
        user.password = hashed_password

        # Add user to database
        session.add(user)
        session.commit()
        session.refresh(user)

        return user

    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while registering the user"
        ) from e

    finally:
        session.close()