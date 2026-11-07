from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class Conversation(BaseModel):
    sender_id: str
    receiver_id: str

class Message(Conversation):
    content: str

# TODO: make websocket message sent validation