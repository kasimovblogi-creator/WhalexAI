from sqlalchemy import select

from app.database.db import async_session
from app.models.user import User


async def get_user(telegram_id: int):

    async with async_session() as session:

        result = await session.execute(
            select(User).where(
                User.telegram_id == telegram_id
            )
        )

        return result.scalar_one_or_none()


async def create_user(
    telegram_id: int,
    username: str | None,
    full_name: str
):

    async with async_session() as session:

        user = User(
            telegram_id=telegram_id,
            username=username,
            full_name=full_name
        )

        session.add(user)

        await session.commit()

        return user