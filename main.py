from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
import logging
import asyncio
from songfinder import SearchSong, DownloadSong
from keyboards import numbers_button
from config import BOT_TOKEN


dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}\nmen Musiqa Topuvchi Botman")

@dp.message()
async def send_song(message: types.Message):
    global songs
    titles = []
    songs = await SearchSong(message.text)
    for number, song in enumerate(songs, start=1):
        titles.append(f"{number}. {song['title']}")
    await message.answer("\n".join(titles), reply_markup=numbers_button())

@dp.callback_query(F.data.in_(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]))
async def numbers(call: types.CallbackQuery):
    await call.answer(cache_time=1)
    print(songs)
    try:
        if call.data == "one":
            song_url = await DownloadSong(songs[0]['song_id'])
            await call.message.answer_audio(types.BufferedInputFile(song_url, filename=songs[0]['title']))
        elif call.data == "two":
            song_url = await DownloadSong(songs[1]['song_id'])
            await call.message.answer_audio(types.BufferedInputFile(song_url, filename=songs[1]['title']))
        elif call.data == "three":
            song_url = await DownloadSong(songs[2]['song_id'])
            await call.message.answer_audio(types.BufferedInputFile(song_url, filename=songs[2]['title']))
        elif call.data == "four":
            song_url = await DownloadSong(songs[3]['song_id'])
            await call.message.answer_audio(types.BufferedInputFile(song_url, filename=songs[3]['title']))
        elif call.data == "five":
            song_url = await DownloadSong(songs[4]['song_id'])
            await call.message.answer_audio(types.BufferedInputFile(song_url, filename=songs[4]['title']))
        elif call.data == "six":
            song_url = await DownloadSong(songs[5]['song_id'])
            await call.message.answer_audio(types.BufferedInputFile(song_url, filename=songs[5]['title']))
        elif call.data == "seven":
            song_url = await DownloadSong(songs[6]['song_id'])
            await call.message.answer_audio(types.BufferedInputFile(song_url, filename=songs[6]['title']))
        elif call.data == "eight":
            song_url = await DownloadSong(songs[7]['song_id'])
            await call.message.answer_audio(types.BufferedInputFile(song_url, filename=songs[7]['title']))
        elif call.data == "nine":
            song_url = await DownloadSong(songs[8]['song_id'])
            await call.message.answer_audio(types.BufferedInputFile(song_url, filename=songs[8]['title']))
        elif call.data == "ten":
            song_url = await DownloadSong(songs[9]['song_id'])
            await call.message.answer_audio(types.BufferedInputFile(song_url, filename=songs[9]['title']))
    except Exception as e:
        print(e)
        await call.message.answer("Musiqa Topilmadi!")


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
