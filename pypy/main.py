from cart import Cart
from item import Item
from stock import Stock
from user import User
from order import Order

#Prints cart in a simple way
def print_cart(cart):
    print("\n------------------CART-------------------")
    for item in cart.cart:
        print(item.name + " " + item.type + " " + str(item.price) + " In cart: " + str(cart.cart[item]) + " Stock: " + str(item.stock))
        print("-----------------------------------------")
    print("\n")
    
def print_inventory(stock):
    print("\n----------------INVENTORY----------------")
    for item in stock.inventory:
        print("Name: " + item)
        print(stock.inventory[item].name + " " 
              + stock.inventory[item].type + " " 
              + str(stock.inventory[item].price) 
              + " Stock: " + str(stock.inventory[item].stock))
        print("-----------------------------------------")
    print("\n")
    
def print_orders(orders):
    print("\n--------------------ORDERS--------------------")
    for user in orders.orders:
        print("User: " + user.username)
        print_cart(orders.orders[user])
        print("-------------------------------------------------")

def main():
    stock = Stock()
        
    stock.add("pants", Item("Addidas Sweats", "Pants", 100, 50))  
    stock.add("shirt", Item("Nike T-Shirt", "Shirts", 100, 25))
    stock.add("beer", Item("Odense Classic", "Drinks", 2, 10000))
    stock.add("laptop", Item("Laptop", "Electronics", 5000, 15))   

    print_inventory(stock)
    
    #Make super simple user
    user = User("user", "secret_password")
    
    #Make cart    
    cart = Cart()
    
    #Add itmes
    cart.add(stock.inventory["pants"], 3)  
    cart.add(stock.inventory["shirt"], 4)
    cart.add(stock.inventory["beer"], 1000)
    cart.add(stock.inventory["laptop"], 2)

    #Print cart and see items in cart and stock
    print_cart(cart)

    #Remove item from cart
    cart.remove(stock.inventory["pants"], 2)

    #Show new cart with removed item and updates stock numbers
    print_cart(cart)

    #Should print only x amount in stock
    cart.add(stock.inventory["laptop"], 1000)
    
    cart.add(stock.inventory["laptop"], 5)
    print_cart(cart)

    #Check inventory is up to date
    print_inventory(stock)
    
    orders = Order()
    orders.make_order(user, cart)
    print_orders(orders)
    
    #2nd user
    user2 = User("user2", "secret_password123")  
    cart2 = Cart()
    cart2.add(stock.inventory["pants"], 6)  
    cart2.add(stock.inventory["shirt"], 19)
    cart2.add(stock.inventory["beer"], 10)
    cart2.add(stock.inventory["laptop"], 6)
    
    orders.make_order(user2, cart2)
    print_orders(orders)
    
if __name__ == '__main__':
    main()
