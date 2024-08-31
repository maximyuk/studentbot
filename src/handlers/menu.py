from aiogram import F, Router, types
from aiogram.filters import Command

from src.keyboards import *
from src.data_base import Database

router = Router()

@router.message(Command("start"))
async def start(message:types.message) -> None:
    db = await Database.setup()
    await message.delete()