# use this hashing for ids
from hashlib import sha256

from auth_repository import (
    get_user_id,
    insert_session,
)
from fastapi import Response
from pwdlib import PasswordHash

from ..core.errors import UserNotFoundError
from .auth_repository import get_user_password
from .auth_schemas import User

# and use this for hashing PASSWORDS.
password_hash = PasswordHash.recommended()
THIRTY_DAYS_IN_SECONDS = 60 * 60 * 24 * 30

def set_session_cookie(
        response: Response, 
        session_id: str,
        session_max_age: int = THIRTY_DAYS_IN_SECONDS,
        secure: bool = True,
    ) -> None:

    response.set_cookie(
        key="session_id",
        value=password_hash.hash(session_id),
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

def add_session_by_username(
        username: str,
        session_id: str,
        csrf_token: str,
    ) -> None:
    insert_session(
        # hash session id but not csrf token cuz browser needs to read the csrf token
        # in its original form
        session_id=sha256(session_id.encode()).hexdigest(),
        csrf_token=csrf_token,
        user_id=get_user_id(username),
    )