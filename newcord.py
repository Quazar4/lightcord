import aiohttp
import asyncio
import time

class DiscordClient:
    def __init__(self, token):
        self.token = token
        self.base_url = 'https://discord.com/api/v9'

    async def request(self, method, endpoint, **kwargs):
        async with aiohttp.ClientSession() as session:
            headers = {'Authorization': f'Bot {self.token}', 'Content-Type': 'application/json'}
            async with session.request(method, f'{self.base_url}/{endpoint}', headers=headers, **kwargs) as response:
                if response.status == 429:  # Rate limited
                    retry_after = int(response.headers.get('Retry-After', '1'))
                    print(f'Rate limited. Retrying after {retry_after} seconds...')
                    await asyncio.sleep(retry_after)
                    return await self.request(method, endpoint, **kwargs)
                elif response.status == 502:  # Bad gateway
                    print('Bad gateway. Retrying after 5 seconds...')
                    await asyncio.sleep(5)
                    return await self.request(method, endpoint, **kwargs)
                else:
                    return await response.json()

    async def sendMessage(self, channel_id, message_content):
        endpoint = f'channels/{channel_id}/messages'
        payload = {'content': message_content}
        return await self.request('POST', endpoint, json=payload)

async def main():
    client = DiscordClient('YOUR_BOT_TOKEN')
    result = await client.sendMessage('CHANNEL_ID', 'Hello, Discord!')

    print(result)

asyncio.run(main())
