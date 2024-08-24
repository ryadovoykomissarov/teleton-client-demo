from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_categories_keyboard(categories):
    buttons = []
    builder = InlineKeyboardBuilder()
    for category in categories:
        ctg_key = "category_"+category
        buttons.append(InlineKeyboardButton(text=category, callback_data=ctg_key))
    
    builder.row(buttons)
    kb_inline = builder.as_markup()
    return kb_inline
    
    