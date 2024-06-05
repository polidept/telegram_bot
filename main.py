from config import TOKEN
from database.models import models_main
import asyncio
from aiogram import Bot, Dispatcher
from handlers.commands import router
import logging
import sys

async def main():
    bot = Bot(token = TOKEN) # Connect
    dp = Dispatcher()
    dp.include_router(router = router)
    await dp.start_polling(bot) # Keepping bot in active condition 
    # await models_main()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
