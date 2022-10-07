class Cart:
    def __init__(self):
        self.cart = {}
        
    def add(self, item, amount):
        if item.stock < 0:
            print("Not in stock")
        elif item.stock < amount:
            print("Only " + str(item.stock) + " " + item.name + "(s)" + " in stock")
        else:
            if amount > 0:
                if item in self.cart:
                    self.cart[item] += amount
                else:
                    self.cart[item] = amount
                item.stock -= amount
            else:
                print("Must be a positive amount")
                
    def remove(self, item, amount):
        if amount > 0:
            if item in self.cart:
                if amount < self.cart[item]:
                    self.cart[item] -= amount
                else:
                    self.cart.pop(item)
            item.stock += amount
        else:
            print("Must be a positive amount")