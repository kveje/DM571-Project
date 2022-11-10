from cart import Cart
from item import Item
from inventory import Inventory
from user import User
from order import Order
import uuid

#Prints cart in a simple way
def print_cart(cart):
    print("\n------------------CART-------------------")
    for item in cart.cart:
        print(item.name + " " + item.type + " " + str(item.price) + " In cart: " + str(cart.cart[item]) + " inventory: " + str(item.inventory))
        print("-----------------------------------------")
    print("\n")
    
def print_inventory(inventory):
    print("\n----------------INVENTORY----------------")
    for item in inventory.inventory: #Item == it's ID
        print("ID: " + str(item))
        print(inventory.inventory[item].name + " " 
              + inventory.inventory[item].type + " " 
              + str(inventory.inventory[item].price) 
              + " inventory: " + str(inventory.inventory[item].inventory))
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
    
    user = User(generate_random_uuid())
    
    inventory = Inventory()
    
    pants = Item(1, "Addidas Sweats", "Pants", 100, 50, "f", "d", "d")
    shirt = Item(2, "Nike T-Shirt", "Shirts", 100, 25, "f", "d", "d")
    beer = Item(3, "Odense Classic", "Drinks", 2, 10000, "f", "d", "d")
    laptop = Item(4, "Laptop", "Electronics", 5000, 15, "f", "d", "d")
    
    inventory.add(pants.id, pants)  
    inventory.add(shirt.id, shirt)
    inventory.add(beer.id, beer)
    inventory.add(laptop.id, laptop )   
    
    user.create_shopping_basket(Cart())  
    user.shopping_basket.update(pants, 3)
    
    print_cart(user.shopping_basket)
    
    #Make cart    
    cart = Cart()
    
    #Add itmes
    cart.update(pants, 3)  
    cart.update(shirt, 4)
    cart.update(beer, 1000)
    cart.update(laptop, 2)

    #Print cart and see items in cart and inventory
    print_cart(cart)

    #Remove item from cart
    cart.remove(pants)

    #Show new cart with removed item and updates inventory numbers
    print_cart(cart)

    #Should print only x amount in inventory
    cart.update(laptop, 1000)
    
    cart.update(laptop, 4)
    
    print_cart(cart)

    '''
    DET HER ER IKKE RETTET TIL FOR AT VIRKE

    '''
    # #Check inventory is up to date
    # print_inventory(inventory)
    
    # orders = Order()
    # orders.make_order(user, cart)
    # print_orders(orders)
    
    # #2nd user
    # user2 = User("user2", "secret_password123")  
    # cart2 = Cart()
    # cart2.add(inventory.inventory["pants"], 6)  
    # cart2.add(inventory.inventory["shirt"], 19)
    # cart2.add(inventory.inventory["beer"], 10)
    # cart2.add(inventory.inventory["laptop"], 6)
    
    # orders.make_order(user2, cart2)
    # print_orders(orders)
    
if __name__ == '__main__':
    main()
