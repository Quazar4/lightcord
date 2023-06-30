import json
import websockets

async def disable_button(websocket, channel_id, message_id, button_id):
    payload = {
        "op": 7,
        "d": {
            "channel_id": channel_id,
            "message_id": message_id,
            "button_id": button_id
        }
    }
    await websocket.send(json.dumps(payload))
