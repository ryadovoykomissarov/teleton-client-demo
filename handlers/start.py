from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from keyboards.all_kb import main_kb

import os
start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    dir = os.path.abspath(os.getcwd())
    filename = dir + '/startmsg.png'
    # await message.answer_photo(photo=FSInputFile(filename), caption='Добро пожаловать на биржу рекламы Teleton! Для поиска рекламы по категориям нажмите кнопку "Купить рекламу"\n\n Подпишитесь на наш информационный канал, чтобы следить за событиями: https://t.me/teletononsight', reply_markup=main_kb(message.from_user.id)) # type: ignore
    await message.answer('Добро пожаловать на биржу рекламы Teleton! Для поиска рекламы по категориям нажмите кнопку "Купить рекламу"', reply_markup=main_kb(message.from_user.id)) # type: ignore
