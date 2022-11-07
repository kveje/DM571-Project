class Cart:
    def __init__(self):
        self.cart = {}
        
    def update(self, item, amount):
        if item.stock < 0:
            print("Not in stock")
        elif item.stock < amount:
            print("Only " + str(item.stock) + " " + item.name + "(s)" + " in stock")
        elif amount > 0:
            if item in self.cart:  #Check if item is in cart already
                old_amount = self.cart[item]
                self.cart[item] = amount 
                
                if old_amount < amount:  #Adjust the stock levels according to an increase or decrease in basket amount of item
                    item.stock +=  (old_amount - amount)
                else:
                    item.stock -= (old_amount - amount)   

            else: #Add item to cart if not in cart
                self.cart[item] = amount 
                item.stock -=  amount
        else:
            print("Must be a positive amount")

    def remove(self, item):
        if item in self.cart:
            item.stock += self.cart[item]
            self.cart.pop(item)
                    
        
        
        
        
        
        
        

                
