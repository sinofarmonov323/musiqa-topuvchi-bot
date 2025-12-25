from io import BytesIO
from  config import API_TOKEN
import asyncio
import aiohttp

async def SearchSong(name: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://songfinder.alwaysdata.net/search-songs",
            params={"query": name, "token": API_TOKEN, "limit": 10}
        ) as response:
            if response.status == 200:
                return await response.json()
            else:
                return {"error": "Failed to retrieve data"}

async def DownloadSong(song_id: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://songfinder.alwaysdata.net/download-song-by-id?id={song_id}") as response:
            if response.ok:
                buffer = BytesIO()
                async for chunk in response.content.iter_chunked(1024):
                    buffer.write(chunk)
                buffer.seek(0)
                return buffer.getvalue()
            else:
                return {"error": response.status, "message": response.url}

# data = asyncio.run(SearchSong("eminem mockingbird"))
# data = asyncio.run(DownloadSong("380750890760670080911221380760840"))

# print(data)
