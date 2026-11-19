from secrets import token_urlsafe

from fastapi import APIRouter, HTTPException, Response
from pwdlib import PasswordHash

from .auth_repository import (
    insert_new_user,
    insert_session,
)
from ..errors import UserAlreadyExistsError, UserNotFoundError
from ..messaging.messaging_schemas import LoginResponse, User
from .auth_services import (
    login_details_valid,
    set_and_store_auth_cookies,
)


password_hash = PasswordHash.recommended()

router = APIRouter(
    prefix="/auth",
)

@router.post("/login", response_model=LoginResponse) # LoginResponse ensures camelCase for response (csrf_token => csrfToken)
def login(response: Response, user: User):
    if not login_details_valid(user):
        raise HTTPException(status_code=401, detail="Invalid login info")

    set_and_store_auth_cookies(
        response=response,
        username=user.username,
    )

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
