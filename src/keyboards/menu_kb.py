from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton, 
    ReplyKeyboardBuilder,
    ReplyKeyboardMarkup
)

def user_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    keyboard = ["Додати 👥", "Видалити 👥", "⬅️ Назад", "Сховати ❌"]

    for button in keyboard:
        builder.add(InlineKeyboardButton(text=button, callback_data=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)
    
