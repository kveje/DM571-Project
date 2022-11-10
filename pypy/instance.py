from cart import Cart
from item import Item
from order import Order
from inventory import Inventory
from user import User

class Instance():
    def __init__(self):
        self.stock = Inventory()
        self.users = []
        self.orders = {}

    def hello(self):
        return {'hello': 'world'}

    def create_user(self,user_id):
        self.users.append(User(user_id))

    def remove_user(self, user):
        self.users.pop(user.id)

    def get_user_list(self):
        lst = []
        for user in self.users:
            lst.append(user.id)
        return lst
    
    def create_order(self, user):
        self.orders[user] = user.shopping_basket
    
    def remove_order(self, user):
        self.orders.pop(user)
    
    def get_orders(self):
        order_lst = []
        for order in self.orders:
            order_lst.append(order)
        return order_lst

    def create_item(self, id, name, price, desciption, photo_url, stock_lvl_local, stock_lvl_supplier, supplier):
        self.stock.add(id, Item(id, name, price, desciption, photo_url, stock_lvl_local, stock_lvl_supplier, supplier))
    
    def create_shopping_basket(self, user):
        user.create_shopping_basket(Cart())
    
    

if __name__ == '__main__':
    inst = Instance()
