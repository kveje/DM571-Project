from classes.basket import Basket
from classes.inventory import Inventory
from classes.item import Item
from classes.order import Order
from classes.user import User


class Client:
    """Object representing an instance of the shopping system"""

    def __init__(self, min_stock_lvl: int):
        self.inventory = Inventory()
        self.users = []
        self.orders = []
        self.min_stock_lvl = min_stock_lvl

    def create_user(self, uid: int, username: str, password: str, mail: str) -> None:
        """Creates a user and append it to the userlist"""
        self.users.append(User(uid, username, password, mail))

    def remove_user(self, user: User) -> None:
        """Removes a user from the userlist"""
        self.users.remove(user)

    def get_user_list(self) -> list:
        """Returns a list of all users"""
        user_list = []
        for user in self.users:
            user_list.append(user.uid)
        return user_list

    def get_user(self, uid: int) -> User:
        """Returns a user referenced by a uid"""
        return next(user for user in self.users if user.uid == uid)

    def create_order(self, user: User) -> Order:
        """Creates an order and append it to the orderlist"""
        order = Order(user)
        self.orders.append(order)
        user.remove_basket()
        return order.order

    def remove_order(self, user: User) -> None:
        """Removes a order from the orderlist"""
        self.orders.pop(user)

    def get_order(self, user: User) -> list:
        """Gets all orders from a specific user"""
        user_order_list = []
        for order in self.orders:
            if order.order["uid"] == user.uid:
                user_order_list.append(order.order)

        return user_order_list

    def get_orders(self) -> list:
        """Gets all orders from the orderlist"""
        # Get the order dict from the Order
        order_list = [order.order for order in self.orders]
        return order_list

    def create_item(self, id, name, price, stock_lvl_local, description, supplier, photo_url) -> None:
        """Creates an item an adds it to the inventory"""
        self.inventory.add(Item(id, name, price, stock_lvl_local, description, supplier, photo_url))

    def get_item(self, item_id: int) -> Item:
        """Returns an item referenced by an item_id"""
        return self.inventory.items[item_id]

    def get_basket_items(self, basket: Basket) -> list:
        """Returns a list of all basket items
        Each item is represented by a dict"""
        item_list = []
        for item in basket.basket.keys():
            item_dict = item.get_item()
            item_dict["amount"] = basket.basket[item]
            item_list.append(item_dict)

        return item_list

    def create_basket(self, user: User) -> None:
        """Creates a basket for the given user"""
        user.create_basket(Basket())

    def get_inventory(self) -> list:
        """Returns a list of all items in the inventory"""
        return self.inventory.get_inventory()
