import aiohttp
import json

async def handle_events(token):
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect('wss://gateway.discord.gg/?v=10&encoding=json') as ws:
            payload = {
                "op": 2,
                "d": {
                    "token": token,
                    "properties": {},
                    "intents": 0,
                    "shard": [0, 1],
                    "presence": {}
                }
            }
            await ws.send_json(payload)

            while True:
                response = await ws.receive()
                if response.type == aiohttp.WSMsgType.TEXT:
                    data = json.loads(response.data)

                    event_type = data.get("t")
                    if event_type == "MESSAGE_CREATE":
                        channel_id = data["d"]["channel_id"]
                        message_id = data["d"]["id"]
                        content = data["d"]["content"]
                        await handle_message_received(channel_id, message_id, content)

async def handle_message_received(channel_id, message_id, content):

    print(f"Received message: {content}")
