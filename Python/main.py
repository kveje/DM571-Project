from client import Client
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from flask_restful import Api, Resource

app = Flask(__name__)
CORS(app)
api = Api(app)

# List of API-keys for authorization purposes
api_key_list = ["123456789", "987654321", "654321987"]


class UserList(Resource):
    """Object for http requests on /users"""

    def get(self):
        """Get a list of all users"""
        # Check for api_key
        if request.headers.get("Authorization") in api_key_list:
            user_list = client.get_user_list()
            print("User list returned:", user_list)
            return make_response(jsonify(user_list), 200)
        # Else return error
        else:
            print("Unauthorized Access")
            return "Unauthorized", 401


class User(Resource):
    """Object for http requests on /user"""

    def post(self):
        """Create a user"""
        req = request.get_json()
        # Check for api_key
        if request.headers.get("Authorization") in api_key_list:
            # If the user already exists throw error
            if req["uid"] in client.get_user_list():
                print("User already exists")
                return "User already exists", 400
            # Try to create user
            try:
                client.create_user(req["uid"])
                print("User created with uid:", req["uid"])
                return "", 201
            except:
                print("Could not create user with uid:", req["uid"])
                return "Bad request", 400
        # If not authorized return error
        else:
            print("Unauthorized Access")
            return "Unauthorized", 401


class Basket(Resource):
    """Object for http requests on /user/<int:uid>/basket"""

    def get(self, uid: int):
        """Get the basket of a user"""
        # Check for api_key
        if request.headers.get("Authorization") in api_key_list:
            # Check for existence of user
            if uid not in client.get_user_list():
                print("No user found with uid:", uid)
                return "No user with the given uid", 400
            # Check whether the user has a basket
            elif not hasattr(client.get_user(uid), "basket"):
                print("The user given by uid:", uid, "has no basket")
                return "User doesn't have a basket", 400
            else:
                # Try to get basket
                try:
                    user = client.get_user(uid)
                    item_list = client.get_basket_items(user.basket)
                    print("The basket of user with uid:", uid, "is returned")
                    return make_response(jsonify(item_list), 200)
                except:
                    print("Could not return basket of user with uid:", uid)
                    return "Bad request", 400
        else:
            print("Unauthorized Access")
            return "Unauthorized", 401

    def post(self, uid: int):
        """Creates or updates a basket of a user"""
        req = request.get_json()
        # Check for api_key
        if request.headers.get("Authorization") in api_key_list:
            # Check whether the user exists
            if uid not in client.get_user_list():
                print("No user found with the uid:", uid)
                return "No user with uid", 400
            else:
                # If the user has no basket, create a basket
                if not hasattr(client.get_user(uid), "basket"):
                    print("Creates a basket for user with uid:", uid)
                    client.create_basket(client.get_user(uid))
                # Try to update the basket
                try:
                    user = client.get_user(uid)
                    item = client.get_item(req["item_id"])
                    if req["item_amount"] > item.stock_lvl_local:
                        return "Amount not in stock", 403
                    else:
                        user.basket.update(item, req["item_amount"])
                        basket = client.get_basket_items(user.basket)
                        print(
                            "Basket for user with uid:",
                            uid,
                            "is updated with",
                            req["item_amount"],
                            "amount of the itemid",
                            req["item_id"],
                        )
                        return basket, 200
                except:
                    print("Could not update basket for user with uid", uid)
                    return "Bad request 123", 400
        else:
            print("Unauthorized Access")
            return "Unauthorized", 401

    def delete(self, uid: int):
        """Removes an item from the basket"""
        req = request.get_json()
        if request.headers.get("Authorization") in api_key_list:
            # Check whether the user exists
            if uid not in client.get_user_list():
                print("No user found with the uid:", uid)
                return "No user with uid", 400
            # If the user has no basket, create a basket
            elif not hasattr(client.get_user(uid), "basket"):
                print("The user has no basket")
                return "No basket found", 403
            else:
                try:
                    user = client.get_user(uid)
                    print(user)
                    item = client.get_item(req["item_id"])
                    print(item)
                    user.basket.remove(item)
                    basket = client.get_basket_items(user.basket)
                    print(basket)
                    return basket, 200
                except:
                    print("Could not remove item from the basket of user with uid", uid)
                    return "Bad request 123", 400
        else:
            print(request.headers.get("Authorization"))
            print("Unauthorized acces")
            return "", 400


class Order(Resource):
    """Object for http requests on /user/<int:uid>/order"""

    def get(self, uid: int):
        """Get"""
        # Check for api_key
        if request.headers.get("Authorization") in api_key_list:
            # Check whether the user exists
            if uid not in client.get_user_list():
                return "No user with id", 400
            # Check whe
            elif not hasattr(client.get_user(uid), "basket"):
                return "User doesn't have a basket", 400
            if uid not in client.orders:
                return "User doesn't have an order made", 400
            else:
                return make_response(jsonify(client.get_basket_items(client.orders[uid])), 200)
        else:
            return "Unauthorized", 401

    def post(self, uid: int):
        """"""
        if request.headers.get("Authorization") in api_key_list:
            if uid not in client.get_user_list():
                return "No user with id", 400
            elif not hasattr(client.get_user(uid), "basket"):
                return "User doesn't have a basket", 400
            else:
                user = client.get_user(uid)
                client.create_order(user)
                return "", 201
        else:
            return "Unauthorized", 401


class Orders(Resource):
    """Object for http requests on /orders"""

    def get(self):
        """Get the entire list of orders"""
        # Check for api_key
        if request.headers.get("Authorization") in api_key_list:
            try:
                order_list = {}
                for id, order in client.orders.items():
                    order_list[id] = client.get_basket_items(order)
                print("Order list:", order_list)
                return make_response(jsonify(order_list), 200)
            except:
                print("Could not return orderlist")
                return "Bad request", 400
        else:
            print("Unauthorized Access")
            return "Unauthorized", 401


class Inventory(Resource):
    """Object for http requests on /inventory"""

    def get(self):
        """Get the inventory list"""
        # Check for api_key
        if request.headers.get("Authorization") in api_key_list:
            inventory_list = client.get_inventory()
            print("Inventory list returned")
            return make_response(jsonify(inventory_list), 200)
        else:
            print("Unauthorized Acces")
            return "Unauthorized", 401


api.add_resource(UserList, "/user-list")
api.add_resource(User, "/user")
api.add_resource(Basket, "/user/<int:uid>/basket")
api.add_resource(Order, "/user/<int:uid>/order")
api.add_resource(Orders, "/orders")
api.add_resource(Inventory, "/inventory")


if __name__ == "__main__":
    client = Client()

    """The following simulates the initialisation of a shopping system, by adding some items and users for illustrative purposes"""
    # Adding basic items
    client.create_item(
        1,
        "Wok",
        20.0,
        5,
        "Den Ægte Pande. Approved af det ægte karryfarvede folk!",
        "A",
        "https://cdn.shopify.com/s/files/1/2807/7652/products/Nexgrill_Pro_Wok_website.png?v=1559905032",
    )
    client.create_item(
        2,
        "Jamie Oliver",
        189.95,
        5,
        "Han laver mad på pander og fik skæld ud af en gonger fordi han ikke stegte gode ris",
        "A",
        "https://upload.wikimedia.org/wikipedia/commons/3/38/Jamie_Oliver_%28cropped%29.jpg",
    )
    client.create_item(
        3,
        "GenbrugsPande",
        2.75,
        5,
        "Denne Pande er genbrugt og god for miljøet. God til vegansk mad",
        "A",
        "https://politiken.dk/imagevault/publishedmedia/4vnqctmr536aotcbtq58/combekk-pander3.jpg",
    )
    client.create_item(
        4,
        "Selvvarmende Pande",
        649.95,
        5,
        "Denne Pande består af en lækker jern-legering, der bliver varm hvis man putter den i stikkontakten",
        "A",
        "https://pandasia.dk/wp-content/uploads/Produkter/Non-food/hot-pot-fondue.jpg.webp",
    )
    client.create_item(
        5,
        "Støbejernspande",
        649.95,
        5,
        "Denne Pande består af en lækker jern-legering - den giver hård jern",
        "A",
        "https://www.kramogkanel.dk/wp-content/uploads/2020/01/1026569-Fiskars-Norden-cast-iron-frying-pan-26cm-1.jpg",
    )
    client.create_item(
        6,
        "Panda",
        1000000.99,
        5,
        "Denne pande er lidt delikat, men af god kinesisk kvalitet",
        "A",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Giant_Panda_2004-03-2.jpg/1280px-Giant_Panda_2004-03-2.jpg",
    )

    # Adding some basic users
    client.create_user(123, "Carsten", "Lkj/62dfg", "carsten@email.dk")
    client.create_user(456, "Kasper", "LIhs752ns", "kasper@email.dk")
    client.create_user(789, "Emil", "GNM812sd", "emil@email.dk")

    app.run(debug=True, threaded=True, port=5000)
