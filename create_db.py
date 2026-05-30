import asyncio

from app.database.db import engine
from app.models.user import Base


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all
        )

    print("Database created 🚀")


asyncio.run(create_tables())