import json
import websockets

async def create_button(websocket, channel_id, message_id, label):
    payload = {
        "op": 6,
        "d": {
            "channel_id": channel_id,
            "message_id": message_id,
            "label": label
        }
    }
    await websocket.send(json.dumps(payload))
