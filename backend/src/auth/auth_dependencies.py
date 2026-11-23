from secrets import token_urlsafe
from typing import Annotated

from fastapi import Depends

from ..core.config import COOKIE_ID_BYTES, CSRF_TOKEN_BYTES
from ..core.dependencies import get_auth_service
from .auth_services import AuthService


def generate_session_id(bytes: int = COOKIE_ID_BYTES) -> str:
    return token_urlsafe(bytes)

def generate_csrf_token(bytes: int = CSRF_TOKEN_BYTES) -> str:
    return token_urlsafe(bytes)

AuthServiceDependency = Annotated[AuthService, Depends(get_auth_service)]