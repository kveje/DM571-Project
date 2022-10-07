class Order:
    def __init__(self):
        self.orders = {}
    
    def make_order(self, user, cart):
        self.orders[user] = cart