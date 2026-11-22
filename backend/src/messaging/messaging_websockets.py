import logging
from collections import defaultdict
from json import JSONDecodeError
from typing import Annotated

from fastapi import APIRouter, Cookie, WebSocket, WebSocketDisconnect, status

from ..core.config import ALLOWED_ORIGINS
from .messaging_repository import (
    get_user_id_by_session_id,
    insert_new_message,
)

# declare route, but future note: maybe not needed since this is websockets not REST.
router = APIRouter()
#TODO: add IDs

# init logger
logger = logging.getLogger(__name__)

class ConnectionManager:
    def __init__(self):
        """
        We're gnna maintain 2 dicts allowing for 2 way lookups, with the tradeoff of memory.
        the 2 way lookups are:
        1. Finding websocket by user_id, useful for sending a message
        2. Finding by websocket, useful for 
        """
        self.connected: dict[WebSocket, int] = {}
        self.user_connections = defaultdict(set)

    def remove_user(self, websocket: WebSocket):
        self.connected.pop(websocket)

    async def add_user(self, websocket: WebSocket, user_id: int):
        try:
            await websocket.accept()
            self.connected[websocket] = user_id
            self.user_connections[user_id] = websocket
        except Exception:
            await websocket.close()
            raise

    async def send_message_to_connection(self, message: dict, target_user_id: int):
        """Sends a message directly to ONE specific user if they are online."""
        
        websocket = self.connected.get(target_user_id)
        if websocket:
            # Send as JSON to keep payload structured
            await websocket.send_json(message)
        else:
            return "User not online."

manager = ConnectionManager()

@router.websocket("/ws/")
async def live_messaging(
    websocket: WebSocket, 
    session_id: Annotated[str | None, Cookie()] = None
):
    try:
        # verify origin since CORS doesn't handle it automatically for ws
        # and also verify session_id
        if websocket.headers.get("origin") not in ALLOWED_ORIGINS or session_id is None:
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)

        user_id = get_user_id_by_session_id(session_id)
        
        # add the connection as well as its user id
        await manager.add_user(
            websocket=websocket,
            user_id=user_id,
        )
    except Exception:
        logger.exception("Failed to connect")
        return 

    try:
        while True:
            try:
                data = await websocket.receive_json()
            except JSONDecodeError:
                pass

            # data recieved at this point
            # have an action key in json incase we need to add more actions later.
            action = data.get("action")
            if action is None:
                send_key_not_found_error_ws(
                    websocket=websocket, 
                    key="action"
                )
                continue

            # see what action is there
            if action == "sendMessage":
                if "content" in action:
                    # add message to db
                    insert_new_message(
                        content=data.get("content"), 
                        sender_id=user_id, 
                        #receiver_id=
                    )
                    # send the new message to the receiver
                    #manager.send_message_to_connection(
                    #    message=,
                    #    target_user_id=,)
                    #
                else:
                    send_key_not_found_error_ws(
                        websocket=websocket, 
                        key="content"
                    )
                    continue

    except WebSocketDisconnect:
        manager.remove_user(websocket)

async def send_key_not_found_error_ws(
        websocket: WebSocket, 
        key: str, 
        template: str = "ERROR: No [key] key in JSON sent."
    ):
    await websocket.send_text(template.replace("[key]", key))