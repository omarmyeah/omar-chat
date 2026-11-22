from secrets import token_urlsafe

from ..core.config import COOKIE_ID_BYTES, CSRF_TOKEN_BYTES


def generate_session_id(bytes: int = COOKIE_ID_BYTES) -> str:
    return token_urlsafe(bytes)

def generate_csrf_token(bytes: int = CSRF_TOKEN_BYTES) -> str:
    return token_urlsafe(bytes)