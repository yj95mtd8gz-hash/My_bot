from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛒 Мои заказы")],
        [KeyboardButton(text="💵 Мой баланс")],
        [KeyboardButton(text="💳 Оплатить покупку")],
        [KeyboardButton(text="📞 Связаться с менеджером")],
        [KeyboardButton(text="ℹ Информация")],
    ],
    resize_keyboard=True
)