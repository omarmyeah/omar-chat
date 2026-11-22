from pydantic import BaseModel, Field


class UserCredentials(BaseModel):
    username: str
    password: str

# keep login and registration schemas seperate incase thye diverge in future, maybe registration might need an email or something.
class LoginParams(UserCredentials):
    pass

class RegistrationParams(UserCredentials):
    pass

class CSRFTokenResponse(BaseModel):
    csrf_token: str = Field(serialization_alias="csrfToken")