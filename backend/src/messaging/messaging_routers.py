from typing import Annotated

from fastapi import APIRouter, Depends  #,HTTPException

from .messaging_repository import get_all_messages
from .messaging_schemas import Conversation

router = APIRouter(
    prefix="/api",
)

@router.get("/messages")
def get_messages(conversation: Annotated[Conversation, Depends()]):
    return get_all_messages(
        sender_id=conversation.sender_id,
        receiver_id=conversation.receiver_id,
    )