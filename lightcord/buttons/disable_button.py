import aiohttp

async def disable_button(token, channel_id, message_id, button_id):
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages/{message_id}/buttons/{button_id}"
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.patch(url, headers=headers, json={}) as response:
            if response.status != 200:
                raise Exception(f"Failed to disable button: {response.status}")
