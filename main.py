import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from os import getenv

bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("WhalexAI ishga tushdi 🚀")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())