from classes.basket import Basket


class Order:
    def __init__(self, basket: Basket):
        self.asd = ""

    def make_order(self, user, cart):
        self.orders[user] = cart

    def remove_order(self, user):
        self.orders.pop(user)
