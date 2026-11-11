from pydantic import BaseModel, Field

class User(BaseModel):
    username: str
    password: str

class Conversation(BaseModel):
    sender_id: str
    receiver_id: str

class Message(Conversation):
    content: str

class LoginResponse(BaseModel):
    csrf_token: str = Field(serialization_alias="csrfToken")

# TODO: make websocket message sent validation