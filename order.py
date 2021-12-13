from transitions import Machine


class Pizza(object):
    pass


class Order(object):
    states = ['big_pizza_order', 'small_pizza_order', 'standart_pizza_order']
    transitions = [
        {'trigger': 'chosen_big_with_cash_payment',
         'source': ['big_pizza_order', 'small_pizza_order', 'standart_pizza_order'],
         'dest': 'cash_payment_for_big_pizza'},
        {'trigger': 'chosen_big_with_card_payment',
         'source': ['big_pizza_order', 'small_pizza_order', 'standart_pizza_order'],
         'dest': 'card_payment_for_big_pizza'},
        {'trigger': 'chosen_small_with_cash_payment',
         'source': ['big_pizza_order', 'small_pizza_order', 'standart_pizza_order'],
         'dest': 'cash_payment_for_small_pizza'},
        {'trigger': 'chosen_small_with_card_payment',
         'source': ['big_pizza_order', 'small_pizza_order', 'standart_pizza_order'],
         'dest': 'card_payment_for_small_pizza'}
    ]

    def __init__(self):
        self.machine = Machine(model=self, states=self.states, transitions=self.transitions, initial='order_created')





order = Order()

order.chosen_small_with_card_payment

print(order.state)
