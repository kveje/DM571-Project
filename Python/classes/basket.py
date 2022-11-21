from classes.item import Item


class Basket():
    """Object representing a basket"""

    def __init__(self):
        self.basket = {}

    def update(self, item: Item, amount: int) -> None:
        """Updates the basket with an item.
        If the item is already in the basket, the amount will be updated."""
        # If the item is not in stock, refuse the update
        if item.stock_lvl_local <= 0:
            print("Not in inventory")
        # If the given amount is not in stock, refuse the update
        elif item.stock_lvl_local < amount:
            print("Only " + str(item.stock_lvl_local) + " " + item.name + "(s)" + " in inventory")
        elif amount > 0:
            self.basket[item] = amount
        # If the given amount is negative, refuse the update
        else:
            print("Must be a positive amount")

    def remove(self, item: Item) -> None:
        """Removes an item from the basket"""
        if item in self.basket:
            self.basket.pop(item)
