class Cart:
    def __init__(self):
        self.cart = {}
        
    def update(self, item, amount):
        if item.stock_lvl_local < 0:
            print("Not in inventory")
        elif item.stock_lvl_local < amount:
            print("Only " + str(item.stock_lvl_local) + " " + item.name + "(s)" + " in inventory")
        elif amount > 0:
            if item in self.cart:  #Check if item is in cart already
                old_amount = self.cart[item]
                self.cart[item] = amount 
                
                if old_amount < amount:  #Adjust the inventory levels according to an increase or decrease in basket amount of item
                    item.stock_lvl_local +=  (old_amount - amount)
                else:
                    item.stock_lvl_local -= (old_amount - amount)   

            else: #Add item to cart if not in cart
                self.cart[item] = amount 
                item.stock_lvl_local -=  amount
        else:
            print("Must be a positive amount")

    def remove(self, item):
        if item in self.cart:
            item.stock_lvl_local += self.cart[item]
            self.cart.pop(item)
                    
        
        
        
        
        
        
        

                
