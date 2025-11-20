import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

from handlers.menu import router as menu_router
from handlers.orders import router as orders_router
from handlers.balance import router as balance_router
from handlers.manager import router as manager_router
from handlers.payments import router as payments_router

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(menu_router)
    dp.include_router(orders_router)
    dp.include_router(balance_router)
    dp.include_router(manager_router)
    dp.include_router(payments_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())