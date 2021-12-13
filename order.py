from transitions import Machine


class Pizza(object):
    pass


class Order(object):
    states = ['big_pizza_order', 'small_pizza_order', 'standart_pizza_order']
    transitions = [
        { 'trigger': 'chosen_big', 'source': 'order_created', 'dest': 'big_pizza_order'},
        {'trigger': 'chosen_small', 'source': 'order_created', 'dest': 'small_pizza_order'},
        {'trigger': 'chosen_standart', 'source': 'order_created', 'dest': 'standart_pizza_order'},
        {'trigger': 'chosen_cash_payment', 'source': ['big_pizza_order', 'small_pizza_order', 'standart_pizza_order'],
         'dest': 'cash_payment'},
        {'trigger': 'chosen_card_payment', 'source': ['big_pizza_order', 'small_pizza_order', 'standart_pizza_order'],
         'dest': 'card_payment'}
    ]

    def __init__(self):
        self.machine = Machine(model=self, states=self.states, transitions=self.transitions, initial='order_created')


