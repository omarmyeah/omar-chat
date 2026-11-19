from pydantic import BaseModel, Field

class Conversation(BaseModel):
    sender_id: int
    receiver_id: int

class Message(Conversation):
    content: str

# TODO: make websocket message sent validation