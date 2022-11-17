from classes.item import Item


class Basket(Item):
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
            # If the item is in the cart -> update amount
            if item in self.basket:
                old_amount = self.basket[item]
                self.basket[item] = amount

                # Adjust the inventory levels according to an increase or decrease in basket amount of item
                if old_amount < amount:
                    item.stock_lvl_local += old_amount - amount
                else:
                    item.stock_lvl_local -= old_amount - amount
            # Add item to cart if not in cart
            else:
                self.basket[item] = amount
                item.stock_lvl_local -= amount
        # If the given amount is negative, refuse the update
        else:
            print("Must be a positive amount")
            return

    def remove(self, item: Item) -> None:
        """Removes an item from the basket"""
        if item in self.basket:
            item.stock_lvl_local += self.basket[item]
            self.basket.pop(item)
