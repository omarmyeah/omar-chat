# use this hashing for ids
from hashlib import sha256

from fastapi import Response
from pwdlib import PasswordHash

from ..core.errors import UserNotFoundError

# and use this for hashing PASSWORDS.
password_hash = PasswordHash.recommended()
THIRTY_DAYS_IN_SECONDS = 60 * 60 * 24 * 30

class AuthService:
    def __init__(
			self, 
            repository,
        ):
        self._repository = repository

    def set_session_cookie(
			self,
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

    def is_login_details_valid(
			self,
            username: str,
            password: str,
        ) -> bool:
        try:
            stored_password = self._repository.get_user_password(username=username)
        except UserNotFoundError:
            # user isn't found
            stored_password = None

        # user is found AND not password is correct.
        return (stored_password and password_hash.verify(password, stored_password))

    def add_session_by_username(
			self,
            username: str,
            session_id: str,
            csrf_token: str,
        ) -> None:
        self._repository.insert_session(
            # hash session id but not csrf token cuz browser needs to read the csrf token
            # in its original form
            session_id=sha256(session_id.encode()).hexdigest(),
            csrf_token=csrf_token,
            user_id=self._repository.get_user_id(username),
        )