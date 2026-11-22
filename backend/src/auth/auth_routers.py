
from typing import Annotated

from fastapi import APIRouter, Cookie, HTTPException, Response
from pwdlib import PasswordHash

from ..errors import UserAlreadyExistsError, SessionNotFoundError
from .auth_schemas import (
    CSRFTokenResponse, 
    LoginParams,
    RegistrationParams,
)
from .auth_dependencies import (
    generate_csrf_token,
    generate_session_id,
)
from .auth_repository import (
    get_csrf_token_by_session_id, 
    insert_new_user,
    delete_session_by_session_id,
)
from .auth_services import (
    add_session_by_username,
    login_details_valid,
    set_session_cookie,
)

password_hash = PasswordHash.recommended()

router = APIRouter(
    prefix="/auth",
)

@router.post("/login", response_model=CSRFTokenResponse) # CSRFTokenResponse ensures camelCase for response (csrf_token => csrfToken)
async def login(response: Response, user: LoginParams):
    # validates login and makes new session

    if not login_details_valid(user):
        raise HTTPException(status_code=401, detail="Invalid login info")

    # generate csrf token and 
    session_id = generate_session_id()
    csrf_token = generate_csrf_token()

    set_session_cookie(
        response=response,
        session_id=session_id,
    )

    add_session_by_username(
        session_id=session_id,
        csrf_token=csrf_token,
        username=user.username,
    )

    return {"csrf_token": csrf_token}

@router.post("/register")
def register(user: RegistrationParams):
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

@router.get("/csrf_token", response_model=CSRFTokenResponse)
def csrf_token(session_id: Annotated[str | None, Cookie()] = None):
    # endpoint that retuns csrf token given session id

    if session_id is None:
        raise HTTPException(status_code=401, detail="Missing session cookie")

    return get_csrf_token_by_session_id(id=session_id)
    
@router.delete("/logout")
def logout(session_id: Annotated[str | None, Cookie()] = None):
    # delete the session
    try:
        delete_session_by_session_id(id=session_id)
    except SessionNotFoundError:
        raise HTTPException(status_code=401, detail="Session doesn't exist")