from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class ConversationQueryParams(BaseModel):
    sender_id: str
    receiver_id: str

class Message(ConversationQueryParams):
    content: str