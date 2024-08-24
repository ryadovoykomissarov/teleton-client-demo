# -*- coding: cp1251 -*-
import asyncio
from create_bot import bot, dp, scheduler
from handlers.start import start_router
from handlers.categories import categories_router
from handlers.callbacks import callback_router

async def main():
    dp.include_routers(start_router, categories_router, callback_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


