from aiogram.utils.callback_data import CallbackData

order_callback = CallbackData("order", "pizza_size")
payment_callback = CallbackData("payment", "payment_method")
accept_callback = CallbackData("accept", "answer")
