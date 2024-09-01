from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton, 
    ReplyKeyboardBuilder,
    ReplyKeyboardMarkup
)

from src.data_base import Database

def user_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    keyboard = ["Додати 👥", "Видалити 👥", "⬅️ Назад", "Сховати ❌"]

    for button in keyboard:
        builder.add(InlineKeyboardButton(text=button, callback_data=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)



async def selection_student_kb() -> InlineKeyboardMarkup:
    db = await Database.setup()
    list_students = await db.member_list()  
    builder = InlineKeyboardBuilder()

    for student in list_students:
        name_member = student  
        builder.add(InlineKeyboardButton(text=name_member, callback_data=name_member))

    return builder.adjust(4).as_markup()

    
