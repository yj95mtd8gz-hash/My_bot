from aiogram import Router, types
from keyboards.main_menu import main_menu

router = Router()

@router.message(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer("Добро пожаловать в магазин! Выберите действие:", reply_markup=main_menu)