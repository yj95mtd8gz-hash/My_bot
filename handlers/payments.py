from aiogram import Router, types

router = Router()

@router.message(lambda msg: msg.text == "💳 Оплатить покупку")
async def pay(message: types.Message):
    await message.answer("Выберите товар для оплаты… (позже подключим платежи)")