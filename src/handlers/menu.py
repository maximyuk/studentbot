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
async def start(message: types.Message) -> None:
    await message.delete()
    await message.answer(text="Нажміть на кнопку", reply_markup = user_kb())
    await state.clear()
    
    
    
    
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
    donate = 0

    await db.add_student_group(name_member = user_message, donate = donate)

    await message.answer("Група додана ✅", reply_markup=None)
    await state.clear()
    
    
@router.message(Command("list"))
async def start(message: types.Message) -> None:
    await message.delete()
    await message.answer(text="Нажміть на кнопку", reply_markup = await selection_student_kb())
    await State.clear()