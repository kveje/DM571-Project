from cart import Cart
from item import Item
from stock import Stock
from user import User
from order import Order
import uuid

#Prints cart in a simple way
def print_cart(cart):
    print("\n------------------CART-------------------")
    for item in cart.cart:
        print(item.name + " " + item.type + " " + str(item.price) + " In cart: " + str(cart.cart[item]) + " Stock: " + str(item.stock))
        print("-----------------------------------------")
    print("\n")
    
def print_inventory(stock):
    print("\n----------------INVENTORY----------------")
    for item in stock.inventory: #Item == it's ID
        print("ID: " + str(item))
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

def generate_random_uuid(): #Skal ikke ligge her, men god måde at lave random uuid's
    return uuid.uuid4()

def main():
    
    user = User(generate_random_uuid(), "kk", "HAHA", "JOJ")

    print(user.id)   
    
    
    
    stock = Stock()
    
    pants = Item(generate_random_uuid(), "Addidas Sweats", "Pants", 100, 50, "f", "d", "d")
    shirt = Item(generate_random_uuid(), "Nike T-Shirt", "Shirts", 100, 25, "f", "d", "d")
    beer = Item(generate_random_uuid(), "Odense Classic", "Drinks", 2, 10000, "f", "d", "d")
    laptop = Item(generate_random_uuid(), "Laptop", "Electronics", 5000, 15, "f", "d", "d")
    
    stock.add(pants.id, pants)  
    stock.add(shirt.id, shirt)
    stock.add(beer.id, beer)
    stock.add(laptop.id, laptop )   

    print_inventory(stock)
    
    #Make cart    
    cart = Cart()
    
    #Add itmes
    cart.update(pants, 3)  
    cart.update(shirt, 4)
    cart.update(beer, 1000)
    cart.update(laptop, 2)

    #Print cart and see items in cart and stock
    print_cart(cart)

    #Remove item from cart
    cart.remove(pants)

    #Show new cart with removed item and updates stock numbers
    print_cart(cart)

    #Should print only x amount in stock
    cart.update(laptop, 1000)
    
    cart.update(laptop, 4)
    
    print_cart(cart)

    '''
    DET HER ER IKKE RETTET TIL FOR AT VIRKE

    '''
    # #Check inventory is up to date
    # print_inventory(stock)
    
    # orders = Order()
    # orders.make_order(user, cart)
    # print_orders(orders)
    
    # #2nd user
    # user2 = User("user2", "secret_password123")  
    # cart2 = Cart()
    # cart2.add(stock.inventory["pants"], 6)  
    # cart2.add(stock.inventory["shirt"], 19)
    # cart2.add(stock.inventory["beer"], 10)
    # cart2.add(stock.inventory["laptop"], 6)
    
    # orders.make_order(user2, cart2)
    # print_orders(orders)
    
if __name__ == '__main__':
    main()
