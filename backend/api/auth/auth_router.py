from fastapi import APIRouter

from db.models.user import User
from service.auth.auth_service import register_user

auth_router = APIRouter()

@auth_router.post("/login", response_model=User)
async def login(user: User):
    """
    Login endpoint for user authentication.

    This endpoint accepts user credentials and returns a token
    upon successful authentication.
    """
    # Here you would typically check the user's credentials
    # and return a token or user object.
    return user

@auth_router.post("/register", response_model=User)
async def register(user: User):
    """
    Registration endpoint for new users.
    """
    return await register_user(user)

@auth_router.post("/logout")
async def logout():
    """
    Logout endpoint to invalidate the user's session.
    """
    # Here you would typically invalidate the user's session
    # or token.
    return {"message": "Logged out successfully"}

@auth_router.post("/refresh")
async def refresh():
    """
    Refresh token endpoint to get a new access token.
    """
    # Here you would typically check the refresh token
    # and return a new access token.
    return {"message": "Token refreshed successfully"}