import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_buttons import choice, payment, accept
from keyboards.inline.callback_datas import order_callback, payment_callback, accept_callback
from loader import dp
from order import Order

order = Order()


@dp.message_handler(Command("create_order"))
async def create_order(message: Message):
    await message.answer(text="Здраствуйте, Какую вы хотите пиццу? Большую или маленькую?",
                         reply_markup=choice)


@dp.callback_query_handler(order_callback.filter(pizza_size=["big", "small", "standart"]))
async def payment_method(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")
    await call.message.answer(text="Как вы будете платить?",
                              reply_markup=payment)


@dp.callback_query_handler(order_callback.filter(pizza_size="big"), payment_callback.filter(payment_method="cash"))
async def buying_big_pizza(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")
    order.chosen_big

    await call.message.answer("Вы хотите большую пиццу, оплата - наличкой?",
                              reply_markup=accept)


@dp.callback_query_handler(accept_callback.filter(answer="yes"))
async def answer_on_yes(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Спасибо за заказ")


@dp.callback_query_handler(accept_callback.filter(answer="no"))
async def answer_on_yes(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Заказ отменен")


@dp.callback_query_handler(text="cancel")
async def cancel_order(call: CallbackQuery):
    await call.answer("Вы отменили заказ", show_alert=True)
    await call.message.edit_reply_markup()

