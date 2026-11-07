from fastapi import APIRouter, HTTPException
from pwdlib import PasswordHash

from ..database.repository import (
    get_user_password,
    insert_new_user,
)
from ..errors import UserAlreadyExistsError, UserNotFoundError
from ..schemas import User

password_hash = PasswordHash.recommended()

router = APIRouter(
    prefix="/auth",
)

@router.post("/login")
def login(user: User):
    # remember to hash.
    try:
        stored_password = get_user_password(user.username)
    except UserAlreadyExistsError:
        stored_password = None
    
    if not stored_password or stored_password != user.password:
        raise HTTPException(status_code=401, detail="Invalid login info")

@router.post("/register")
def register(user: User):
    try:
        new_user = insert_new_user(user)
        return {
            "id": new_user.id,
        }
    except UserAlreadyExistsError:
        return HTTPException(
            status_code=409,
            detail="Username already taken.",
        )
