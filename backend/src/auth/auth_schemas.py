from pydantic import BaseModel, Field

class User(BaseModel):
    username: str
    password: str

class CSRFTokenResponse(BaseModel):
    csrf_token: str = Field(serialization_alias="csrfToken")