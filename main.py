import asyncio

from aiogram import Bot
from aiogram import Dispatcher

from app.handlers.start import router
from app.utils.config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

dp.include_router(router)


async def main():

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())