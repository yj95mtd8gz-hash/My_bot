from aiogram import Router, types

router = Router()

@router.message(lambda msg: msg.text == "🛒 Мои заказы")
async def show_orders(message: types.Message):
    await message.answer("Ваши заказы:\n• №1234 – в обработке\n• №5678 – доставлен")