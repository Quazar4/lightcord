import aiohttp

async def get_channel(token, channel_id):
    url = f"https://discord.com/api/v10/channels/{channel_id}"
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status != 200:
                raise Exception(f"Failed to get channel: {response.status}")
            
            data = await response.json()
            return data
