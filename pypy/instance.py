from cart import Cart
from item import Item
from order import Order
from inventory import Inventory
from user import User
import copy

class Instance():
    def __init__(self):
        self.inventory = Inventory()
        self.users = []
        self.orders = {}

    def hello(self):
        return {'hello': 'world'}

    def create_user(self,user_id):
        self.users.append(User(user_id))

    def remove_user(self, user):
        self.users.remove(user)

    def get_user_list(self):
        lst = []
        for user in self.users:
            lst.append(user.id)
        return lst
    
    def get_user(self, user_id):
        return next(user for user in self.users if user.id == user_id)
        
    def create_order(self, user):
        self.orders[user.id] = copy.deepcopy(user.shopping_basket)
        
    def remove_order(self, user):
        self.orders.pop(user)
    
    def get_orders(self):
        order_lst = []
        for order in self.orders:
            order_lst.append(order)
        return order_lst

    def create_item(self, id, name, price, stock_lvl_local, description, supplier, photo_url):
        self.inventory.add(Item(id, name, price, stock_lvl_local, description, supplier, photo_url))
    
    def get_item(self, item_id):
        return self.inventory.items[item_id]
    
    def get_basket_items(self, basket):
        item_list = []
        for item in basket.cart:
            item_list.append(item.get_item())
        return item_list
              
    def create_shopping_basket(self, user):
        user.create_shopping_basket(Cart())
    
    

if __name__ == '__main__':
    inst = Instance()
