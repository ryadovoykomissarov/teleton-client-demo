from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
# from create_bot import admins
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main_kb(user_tgid: int):
    kb_list = [
        [KeyboardButton(text="Купить рекламу")]
    ]
    # if user_tgid in admins:
    #     kb_list.append([KeyboardButton(text="Администрирование")])
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list, 
        resize_keyboard=True, 
            one_time_keyboard=True,
            input_field_placeholder="Воспользуйтесь меню:")
    return keyboard

def admin_kb():
    kb_list = [
        [KeyboardButton(text="Добавить категорию"),
         KeyboardButton(text="Удалить категорию"),
         KeyboardButton(text="Добавить канал"),
         KeyboardButton(text="Удалить канал")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list,
                                   resize_keyboard=True,
                                   one_time_keyboard=True,
                                   input_field_placeholder="А ты правда админ?..")
    return keyboard