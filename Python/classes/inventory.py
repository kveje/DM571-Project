from classes.item import Item


class Inventory:
    """Object representing the inventory"""

    def __init__(self):
        self.items = {}

    def add(self, item: Item) -> None:
        """Adds an item to the inventory"""
        self.items[item.id] = item

    def remove(self, id: int) -> None:
        """Removes an item from the inventory"""
        self.items.pop(id)

    def update_stock_lvl(self, id: int, qty: int) -> None:
        """Updates the stock level for a given item"""
        self.items[id].set_stock_lvl_local = qty

    def get_inventory(self) -> list:
        """Get a list of the current inventory"""
        inventory_list = []
        for i in self.items:
            inventory_list.append(self.items[i].get_item())
        return inventory_list
