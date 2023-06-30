import aiohttp

async def create_channel(token, guild_id, name):
    url = f"https://discord.com/api/v10/guilds/{guild_id}/channels"
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": name
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            if response.status != 201:
                raise Exception(f"Failed to create channel: {response.status}")
            
            data = await response.json()
            return data
