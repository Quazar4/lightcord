import aiohttp

async def edit_message(token, channel_id, message_id, content):
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages/{message_id}"
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "content": content
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.patch(url, headers=headers, json=payload) as response:
            if response.status != 200:
                raise Exception(f"Failed to edit message: {response.status}")
