import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from app.handlers import router

load_dotenv()
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot=bot)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        dp.include_router(router)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
