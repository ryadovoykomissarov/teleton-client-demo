from decouple import config
from create_bot import bot

async def newSellerNotification(seller_tg_id, seller_channel_link, seller_price):
    message = "Пользователь: " + str(seller_tg_id) + "\nСсылка на канал: " + seller_channel_link + "\nЦена: " + seller_price
    admin_id=config('ADMIN')
    await bot.send_message(chat_id=admin_id, text=message)