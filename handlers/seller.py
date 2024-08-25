from aiogram import Router, F
from aiogram.types import Message

import keyboards.inline_kbs as inline_kbs
import db.model.categories_model as categories_model
import db.db_handler as db

from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from workers.w_json import get_categories
from workers.w_notifications import newSellerNotification

class FillSellerForm(StatesGroup):
    channel_link = State()
    ad_price = State()

seller_router = Router()

@seller_router.message(F.text.contains('Я продаю рекламу'), StateFilter(default_state))
async def msg_sell_ad(message: Message, state: FSMContext):
    await message.reply(text='Отправьте ссылку на Telegram канал, который собираетесь разместить')
    await state.set_state(FillSellerForm.channel_link)

@seller_router.message(StateFilter(FillSellerForm.channel_link), F.text.isalpha())
async def fill_channel_link(message: Message, state: FSMContext):
    await state.update_data(channel_link=message.text)
    await message.answer(text='Теперь введите ценовую политику для размещения рекламы на Вашей площадке. Например: Пост - 1/24 - 7500р')
    await state.set_state(FillSellerForm.ad_price)

@seller_router.message(StateFilter(FillSellerForm.ad_price), F.text.isalpha())
async def fill_ad_price(message: Message, state: FSMContext):
    await state.update_data(ad_price=message.text)
    data = await state.get_data()
    await state.clear()

    seller_id = message.from_user.id
    channel_link = data.get('channel_link')
    seller_price = data.get('ad_price')

    await newSellerNotification(seller_tg_id=seller_id, seller_channel_link=channel_link, seller_price=seller_price)
    
    await message.answer( 'Спасибо!\nИнформация о Вашем канале передана на модерацию. После успешной модерации информация о канале будет добавлена в выдачу.')