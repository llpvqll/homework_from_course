import aiohttp
import asyncio
import json

FILENAME = 'special_file1.json'
URL = ["https://docs.python.org/3/library/urllib.request.html#module-urllib.request",
       "https://www.youtube.com/",
       "https://github.com/"]

DATA = []


async def main():
    for item in URL:
        async with aiohttp.ClientSession() as session:
            async with session.get(item) as response:
                html = await response.text()
                DATA.append({response.status: html[:290]})

    with open(FILENAME, 'w', encoding='utf-8', newline='') as file:
        json.dump(DATA, file)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
