from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import order_callback, payment_callback

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Большую", callback_data="order:big"),
            InlineKeyboardButton(text="Маленькую", callback_data="order:small"),
            InlineKeyboardButton(text="Стандартную", callback_data="order:standart")
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="cancel")
        ]
    ]
)

payment = InlineKeyboardMarkup(
    inline_keyboard=[
            [
                InlineKeyboardButton(text="Наличными", callback_data="payment:cash"),
                InlineKeyboardButton(text="Картой", callback_data="payment:card")
            ],
            [
                InlineKeyboardButton(text="Отмена", callback_data="cancel")
            ]
        ]
)

accept = InlineKeyboardMarkup(
    inline_keyboard=[
            [
                InlineKeyboardButton(text="Да", callback_data="answer:yes"),
                InlineKeyboardButton(text="Нет", callback_data="answer:no")
            ]
    ]
)