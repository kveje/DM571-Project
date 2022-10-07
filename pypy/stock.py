class Stock:
    def __init__(self):
        self.inventory = {}
        
    def add(self, item_name, item_object):
        self.inventory[item_name]=item_object
        