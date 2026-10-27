from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..database.repository import get_user_password
from .passwords import password_hash
from ..schemas import User

router = APIRouter(
    prefix="/auth",
)

@router.post("/login")
def login(user: User):
    # remember to hash.
    if get_user_password(user.username) != user.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid login info"
        )

@router.post("/register")
def register(user: User):
    ...