import unittest

# from classes.basket import Basket
# from classes.inventory import Inventory
# from classes.item import Item
# from classes.order import Order
# from classes.user import User
def get_stock_lvl_supplier_A(id: int) -> int:
    """Function for communicating with Supplier A's API"""
    # Here should be some logic for calling the supplier API
    if id < 3:
        return 20
    else:
        return 10


def get_stock_lvl_supplier_B(id: int) -> int:
    """Function for communicating with Supplier B's API"""
    # Here should be some logic for calling the supplier API
    if id > 3:
        return 10
    else:
        return 20


def order_from_supplier_A(id: int, amount: int) -> int:
    """Function for ordering from supplier B"""
    stock_lvl_supplier = get_stock_lvl_supplier_A(id)
    if amount > stock_lvl_supplier:
        # Some logic for ordering from supplier
        return stock_lvl_supplier
    else:
        # Some logic for ordering from supplier
        return amount


def order_from_supplier_B(id: int, amount: int) -> int:
    """Function for ordering from supplier B"""
    stock_lvl_supplier = get_stock_lvl_supplier_B(id)
    if amount > stock_lvl_supplier:
        # Some logic for ordering from supplier
        return stock_lvl_supplier
    else:
        # Some logic for ordering from supplier
        return amount


class Item:
    """Item class, that handles item stuff"""

    def __init__(
        self, id: int, name: str, price: int, stock_lvl_local: int, description: str, supplier: str, photo_url: str
    ):
        self.id = id
        self.name = name
        self.price = price
        self.stock_lvl_local = stock_lvl_local
        self.description = description
        self.supplier = supplier
        self.photo_url = photo_url

    def get_supplier_lvl(self) -> int:
        """Returns the updated item information in a dict"""
        if self.supplier == "A" or self.supplier == "a":
            return get_stock_lvl_supplier_A(self.id)
        elif self.supplier == "B" or self.supplier == "b":
            return get_stock_lvl_supplier_B(self.id)

    def get_item(self) -> dict:
        """Returns the updated item information in a dict"""
        stock_lvl_supplier = self.get_supplier_lvl()
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock_lvl_local": self.stock_lvl_local,
            "stock_lvl_supplier": stock_lvl_supplier,
            "description": self.description,
            "supplier": self.supplier,
            "photo_url": self.photo_url,
        }

    def get_stock_lvl_local(self) -> int:
        return self.stock_lvl_local

    def inc_stock_lvl_local(self, inc: int) -> None:
        """Setter for local stock level value"""
        self.stock_lvl_local += inc

    def order_from_supplier(self, amount) -> None:
        """Orders an amount of the item from the supplier"""
        if self.supplier == "A" or self.supplier == "a":
            ordered_amount = order_from_supplier_A(self.id, amount)
            self.stock_lvl_local += ordered_amount
        elif self.supplier == "B" or self.supplier == "b":
            ordered_amount = order_from_supplier_B(self.id, amount)
            self.stock_lvl_local += ordered_amount


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

class User():
    """Object representing a user"""

    def __init__(self, uid: int, name: str, password: str, mail: str):
        self.uid = uid
        self.name = name
        self.password = password
        self.mail = mail

    def create_basket(self, basket: Basket) -> None:
        """Creates a shoppingbasket for the given user"""
        self.basket = basket

    def remove_basket(self) -> None:
        delattr(self, "basket")



class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User(123, "Carsten", "Lkj/62dfg", "carsten@email.dk")
        self.user.create_basket(Basket())
        
    def test_user_creation(self):
        self.assertEqual(self.user.uid, 123)
        self.assertEqual(self.user.name, "Carsten")
        self.assertEqual(self.user.password, "Lkj/62dfg")
        self.assertEqual(self.user.mail, "carsten@email.dk")
    
    def test_basket(self):
        self.assertTrue(hasattr(self.user, "basket"))
        
    def test_remove_basket(self):
        self.user.remove_basket()
        self.assertFalse(self.user, "basket")
        
        
if __name__ == '__main__':
    unittest.main()