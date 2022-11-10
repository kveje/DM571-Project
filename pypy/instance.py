from cart import Cart
from item import Item
from order import Order
from stock import Stock
from user import User

class Instance():
    def __init__(self):
        self.stock = Stock()
        self.users = []

    def createUser(self,user_id,username):
        self.users.append(User(1,'Emil'))

    def getUserList(self):
        lst = []
        for i in self.users:
            lst.append(i)
        return lst

if __name__ == '__main__':
    inst = Instance()
