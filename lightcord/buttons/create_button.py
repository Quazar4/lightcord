import aiohttp

async def create_button(token, channel_id, message_id, label):
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages/{message_id}/buttons"
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "label": label
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            if response.status != 201:
                raise Exception(f"Failed to create button: {response.status}")
