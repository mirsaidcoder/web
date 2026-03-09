from aiogram import Dispatcher
from loader import bot, dp
from handlers import register_all_handlers

async def main():
    register_all_handlers(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())