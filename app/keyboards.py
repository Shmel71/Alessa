from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="first"),KeyboardButton(text="second")]
], resize_keyboard=True, input_field_placeholder="Какойто текст")
