from fastapi import APIRouter, Depends, HTTPException, status
from core.security import verify_password, create_access_token
from endpoints.depends import get_user_repository
from models.token import Token, Login
from repository.users import UserRepository
router = APIRouter()


@router.post("/", response_model=Token)
async def login(
        login: Login,
        users: UserRepository = Depends(get_user_repository)
):
    user = await users.get_by_email(email=login.email)
    if user is None or not verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    return Token(
        access_string=create_access_token({"sub": user.email}),
        token_type="Bearer"
    )