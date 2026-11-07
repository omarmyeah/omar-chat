from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from json import JSONDecodeError
from ..database.repository import insert_new_message

router = APIRouter()
#TODO: add IDs

class ConnectionManager:
    def __init__(self):
        self.connected: dict[str, WebSocket] = {}

    def remove_user(self, websocket: WebSocket):
        self.connected.remove(websocket)

    async def add_user(self, websocket: WebSocket):
        try:
            await websocket.accept()
            self.connected.add(websocket)
        except Exception:
            await websocket.close()
            raise

    async def send_message_to_connection(self, message: dict, target_user_id: str):
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
        await manager.add_user(websocket)
    except Exception:
        print("Failed to connect")
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
            if "action" is None:
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

def send_key_not_found_error_ws(
        websocket: WebSocket, 
        key: str, 
        template: str = "ERROR: No [key] key in JSON sent."
    ):
    websocket.send_text(template.replace("[key]", key))