import logging
from json import JSONDecodeError

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from .messaging_repository import insert_new_message

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
        self.user_connections: dict[int, set[WebSocket]] = {}

    def remove_user(self, websocket: WebSocket):
        self.connected.pop(websocket)

    async def add_user(self, websocket: WebSocket, user_id: int):
        try:
            await websocket.accept()
            self.connected[websocket] = user_id
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

@router.websocket("/ws/{client_id}")
async def live_messaging(websocket: WebSocket, client_id: int):
    try:
        # id param required here, do this after auth
        await manager.add_user(websocket)
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
                    insert_new_message(content=data.get("content"), 
                        sender_id=client_id, 
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