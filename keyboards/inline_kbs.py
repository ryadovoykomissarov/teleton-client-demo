from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_categories_keyboard(categories):
    builder = InlineKeyboardBuilder()
    for category in categories:
        ctg_key = "category_"+category
        builder.button(text=category, callback_data=ctg_key)
    
    kb_inline = builder.as_markup()
    return kb_inline
    
    