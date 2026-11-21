from secrets import token_urlsafe

from ..config import COOKIE_ID_BYTES, CSRF_TOKEN_BYTES

def generate_session_id() -> str:
    return token_urlsafe(COOKIE_ID_BYTES)

def generate_csrf_token() -> str:
    return token_urlsafe(CSRF_TOKEN_BYTES)