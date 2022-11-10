class Inventory:
    def __init__(self):
        self.inventory = {}
        
    def add(self, id, item_object):
        self.inventory[id] = item_object
        
    def remove(self, id):
        self.inventory.pop(id)
        