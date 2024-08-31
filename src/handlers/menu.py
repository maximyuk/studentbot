from aiogram import F, Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start(message:types.message) -> None:
    await message.delete()