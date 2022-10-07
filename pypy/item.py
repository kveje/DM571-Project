from unicodedata import name


class Item:
    def __init__(self, name, type, price, stock):
        self.name = name
        self.type = type
        self.price = price
        self.stock = stock
