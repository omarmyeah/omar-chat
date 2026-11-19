from fastapi import Response, Depends
from ..errors import UserNotFoundError
from .auth_repository import get_user_password
from pwdlib import PasswordHash
from .auth_schemas import User
from typing import Annotated
from secrets import token_urlsafe
from auth_repository import (
    insert_session,
    get_user_id,
)
from ..config import COOKIE_ID_LENGTH, CSRF_TOKEN_LENGTH

password_hash = PasswordHash.recommended()
THIRTY_DAYS_IN_SECONDS = 60 * 60 * 24 * 30

def set_and_store_auth_cookies(
        response: Response, 
        username: str,
        csrf_token: Annotated[str, Depends(lambda: token_urlsafe(CSRF_TOKEN_LENGTH))],
        session_id: Annotated[str, Depends(lambda: token_urlsafe(COOKIE_ID_LENGTH))],
        csrf_max_age: int = THIRTY_DAYS_IN_SECONDS, # 1 month
        session_max_age: int = THIRTY_DAYS_IN_SECONDS,
        secure: bool = True,
    ) -> None:

    # add to db.

    insert_session(
        session_id=session_id,
        csrf_token=csrf_token,
        user_id=get_user_id(username=username),
    )

    response.set_cookie(
        key="csrf_token",
        value=csrf_token,

        # js needs to access this:
        httponly=False,
        secure=secure,
        samesite="lax",
        max_age=csrf_max_age,
    )

    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True,
        secure=secure,
        samesite="lax",
        max_age=session_max_age,
    )

def login_details_valid(user: User):
    try:
        stored_password = get_user_password(user.username)
    except UserNotFoundError:
        # user isn't found
        stored_password = None

    # user is found AND not password is correct.
    return (stored_password and password_hash.verify(user.password, stored_password))