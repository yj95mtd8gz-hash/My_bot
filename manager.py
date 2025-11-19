from aiogram import Router, types

router = Router()

@router.message(lambda msg: msg.text == "📞 Связаться с менеджером")
async def contact_manager(message: types.Message):
    await message.answer("Менеджер свяжется с вами в ближайшее время.")