from fastapi import APIRouter, Depends
from typing import List
from models.user import User, UserIn
from repository.users import UserRepository
from .depends import get_user_repository

router = APIRouter()


@router.get("/", response_model=List[User])
async def read_users(
        users: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        skip: int = 100):

    return await users.get_all(limit=limit, skip=0)

@router.post("/", response_model=User)
async def create_user(
        user: UserIn,
        users: UserRepository = Depends(get_user_repository)):

    return await users.create(u=user)

@router.patch("/", response_model=User)
async def update_user(
        id: int,
        user: UserIn,
        users: UserRepository = Depends(get_user_repository)):
    return await users.update(id=id, u=user)

