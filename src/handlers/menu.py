from aiogram import F, Router, types
from aiogram.filters import Command

from src.keyboards import *
from src.data_base import Database

from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class FSMSuperUserPanel(StatesGroup):
    add_member_name = State()
    



router = Router()

@router.message(Command("start"))
async def start(query: types.CallbackQuery) -> None:
    db = await Database.setup()
    await message.delete()
    await query.message.edit_text(
        "123 ⬇️", reply_markup=await user_kb()
    )
    
    
    
    
@router.callback_query(F.data == "Додати 👥")
async def add_student(query: types.CallbackQuery, state: FSMContext):
    await query.message.edit_text(
        "Введіть прізвише та ім'я учасника ⬇️", reply_markup=None
    )
    await state.set_state(FSMSuperUserPanel.add_member_name)


@router.message(F.text, FSMSuperUserPanel.add_member_name)
async def add_student2(message: types.Message, state: FSMContext):
    db = await Database.setup()
    user_message = message.text

    await db.add_student_group(user_message)

    await message.answer("Група додана ✅", reply_markup=None)
    await state.clear()