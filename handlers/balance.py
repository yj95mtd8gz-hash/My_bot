from aiogram import Router, types

router = Router()

@router.message(lambda msg: msg.text == "💵 Мой баланс")
async def show_balance(message: types.Message):
    balance = 1500
    await message.answer(f"Ваш баланс: {balance} ₽")