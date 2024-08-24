from aiogram import Router, F
from aiogram.types import Message

import keyboards.inline_kbs as inline_kbs
import db.model.categories_model as categories_model
import db.db_handler as db

from workers.w_json import get_categories

categories_router = Router()

@categories_router.message(F.text.contains('Купить рекламу'))
async def msg_buy_ad(message: Message):
    # (!) ТОЧКА РАСШИРЕНИЯ - подключение к базе данных
    # connection = await db.get_connection()
    # categories = await categories_model.get_categories(connection=connection)
    known_categories = get_categories()
    inline_kb = inline_kbs.get_categories_keyboard(categories=known_categories)

    await message.reply(text='Выберите подходящую категорию', reply_markup=inline_kb)