from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.services.user_service import (
    get_user,
    create_user
)

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):

    user = await get_user(
        message.from_user.id
    )

    if not user:

        await create_user(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            full_name=message.from_user.full_name
        )

    await message.answer(
        "🚀 WhalexAI ga xush kelibsiz!\n\n"
        "📊 Crypto\n"
        "📈 Forex\n"
        "🥇 Gold\n\n"
        "AI yordamida professional analiz oling."
    )