import aiohttp

async def delete_channel(token, channel_id):
    url = f"https://discord.com/api/v10/channels/{channel_id}"
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.delete(url, headers=headers) as response:
            if response.status != 204:
                raise Exception(f"Failed to delete channel: {response.status}")
