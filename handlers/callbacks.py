import asyncio
from aiogram.utils.chat_action import ChatActionSender
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, LinkPreviewOptions
from workers.w_json import get_channels_by_cat

callback_router = Router()

@callback_router.callback_query(F.data.startswith('category_'))
async def category_cb_handler(call: CallbackQuery):
    await call.answer()
    category = call.data.split("_")[1] # type: ignore
    print(category)
    channels = get_channels_by_cat(category)
    print(channels)
    message = ""
    for ch in channels:
        row = "<a href='"+ch['link']+"'>"+ch['name']+"</a>\n"+"Количество подписчиков: " + ch['subs'] + "\nСтоимость рекламы: " + ch['price']+ "\n\n"
        print(row)
        message = message+row
    
    await call.message.answer(text=message, parse_mode='HTML', link_preview_options=LinkPreviewOptions(is_disabled=True)) # type: ignore