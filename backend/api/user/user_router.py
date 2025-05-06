from typing import Annotated
from fastapi import Depends, APIRouter
from app.db.auth_db.models.user import User
from service.user.user_service import get_current_user

user_router = APIRouter()

@user_router.get("/account", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user

@user_router.get("/account/items")
async def read_own_items(current_user: Annotated[User, Depends(get_current_user)]):
    return [{"item_id": "Foo", "owner": current_user.username}]