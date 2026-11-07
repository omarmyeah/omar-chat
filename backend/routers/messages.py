from fastapi import APIRouter, HTTPException, Depends
from ..schemas import ConversationQueryParams
from ..database.repository import get_all_messages

router = APIRouter(
    prefix="/api",
)

@router.get("/messages")
def get_messages(conversation: ConversationQueryParams = Depends()):
    return get_all_messages(
        sender_id=conversation.sender_id,
        receiver_id=conversation.receiver_id,
    )