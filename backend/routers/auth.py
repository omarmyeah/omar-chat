from fastapi import APIRouter, HTTPException, Response
from pwdlib import PasswordHash
from secrets import token_urlsafe

from ..database.repository import (
    get_user_password,
    insert_new_user,
)
from ..errors import UserAlreadyExistsError, UserNotFoundError
from ..schemas import User, LoginResponse

password_hash = PasswordHash.recommended()

router = APIRouter(
    prefix="/auth",
)

@router.post("/login", response_model=LoginResponse)
def login(response: Response, user: User):
    # remember to hash.
    try:
        stored_password = get_user_password(user.username)
    except UserNotFoundError:
        # user isn't found
        stored_password = None
    
    if not stored_password or not password_hash.verify(user.password, stored_password):
        raise HTTPException(status_code=401, detail="Invalid login info")

    # this is the cookie id, first send a cookie with this as http header, then put this id in db.
    cookie_value = token_urlsafe(32)

    # also csrf token to return.
    csrf_token = token_urlsafe(32)

    response.set_cookie(
        key="session_id",
        value=cookie_value,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=60 * 60 * 24 * 7
    )


    # send only csrf token in body, cookie in header.
    return {"csrf_token": csrf_token}

@router.post("/register")
def register(user: User):
    try:
        new_user = insert_new_user(
            username=user.username,
            password=password_hash.hash(user.password)
        )
        return {
            "id": new_user.id,
        }
    except UserAlreadyExistsError:
        return HTTPException(
            status_code=409,
            detail="Username already taken.",
        )
