import asyncio
import logging

import aiogram
from aiogram import Bot, Dispatcher

from src.config import TOKEN


from src.handlers import (
    menu
)


async def register_handlers(dp: aiogram.Dispatcher) -> None:
    dp.include_router(menu.router)


async def start_bot() -> None:
    bot = Bot(token= TOKEN)
    dispatcher = Dispatcher()
    
    await register_handlers(dispatcher)
    
    await bot.delete_webhook(drop_pending_updates = True)
    await dispatcher.start_polling(bot)
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start_bot())