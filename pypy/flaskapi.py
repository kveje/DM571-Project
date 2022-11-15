from flask import Flask, jsonify, request, make_response, json
from flask_restful import Resource, Api
from flask_cors import CORS
from client import Client

app = Flask(__name__)
CORS(app)
api = Api(app)

AUTH = "123456789"

class UserList(Resource):
    def get(self):
        if request.headers.get('Authorization') == AUTH:
           return make_response(jsonify(client.get_user_list()), 200)
        else:
           return "Unauthorized", 400

class User(Resource):
    def post(self):
        req = request.get_json()
        if request.headers.get('Authorization') == AUTH:
            if req['uid'] in client.get_user_list():
                return "User already exists", 400
            try:
                client.create_user(req["uid"])
                return "", 201
            except:
                return "Bad request", 400
        else:
           return "Unauthorized", 401

class Basket(Resource):
    def get(self, uid):
        if request.headers.get('Authorization') == AUTH:
            if uid not in client.get_user_list():
                return "No user with id", 400
            elif not hasattr(client.get_user(uid), 'shopping_basket'):
                return "User doesn\'t have a basket", 400
            else:
                try:
                    user = client.get_user(uid)
                    item_list = client.get_basket_items(user.shopping_basket)    
                    return make_response(jsonify(item_list), 200)
                except:
                    return "Bad request", 400
        else:
            return "Unauthorized", 401

    def post(self, uid):
        req = request.get_json()
        if request.headers.get('Authorization') == AUTH:
            if uid not in client.get_user_list():
                return "No user with id", 400
            else:
                if not hasattr(client.get_user(uid), 'shopping_basket'):
                    client.create_shopping_basket(client.get_user(uid))
                try:
                    user = client.get_user(uid)
                    item = client.get_item(req['item_id'])
                    user.shopping_basket.update(item, req['item_amount'])
                    return "", 200
                except:
                    return "Bad request", 400
        else:
            return "Unauthorized", 401

class Order(Resource):
    def get(self, uid):
        if request.headers.get('Authorization') == AUTH:
            if uid not in client.get_user_list():
                return "No user with id", 400
            elif not hasattr(client.get_user(uid), 'shopping_basket'):
                return "User doesn\'t have a basket", 400
            if uid not in client.orders:
                return "User doesn\'t have an order made", 400
            else:
                return make_response(jsonify(client.get_basket_items(client.orders[uid])), 200)
        else:
           return "Unauthorized", 400

    def post(self, uid):
        if request.headers.get('Authorization') == AUTH:
            if uid not in client.get_user_list():
                return "No user with id", 400
            elif not hasattr(client.get_user(uid), 'shopping_basket'):
                return "User doesn\'t have a basket", 400
            else:
                user = client.get_user(uid)
                client.create_order(user)
                return "", 201
        else:
           return "Unauthorized", 400


class Orders(Resource):
    def get(self):
        if request.headers.get('Authorization') == AUTH:
            order_list = {}
            for id, order in client.orders.items():
                order_list[id] = client.get_basket_items(order)

            return make_response(jsonify(order_list), 200)
        else:
           return "Unauthorized", 400


class Inventory(Resource):
    def get(self):
        if request.headers.get('Authorization') == AUTH:
            inventory_list = client.get_inventory()
            print(request.headers)
            return {"data" : inventory_list}, 200
        else:
            return "Unathorized", 400

api.add_resource(UserList, '/user-list')
api.add_resource(User, '/user')
api.add_resource(Basket, '/user/<int:uid>/basket')
api.add_resource(Order, '/user/<int:uid>/order')
api.add_resource(Orders, '/orders')
api.add_resource(Inventory, '/inventory')


if __name__ == '__main__':
    client = Client()

    # Adding basic items
    client.create_item(1, "Wok", 20.0, 5, "Den Ægte Pande. Approved af det ægte karryfarvede folk!", "A","https://cdn.shopify.com/s/files/1/2807/7652/products/Nexgrill_Pro_Wok_website.png?v=1559905032")
    client.create_item(2, "Jamie Oliver", 189.95, 5, "Han laver mad på pander og fik skæld ud af en gonger fordi han ikke stegte gode ris","A","https://upload.wikimedia.org/wikipedia/commons/3/38/Jamie_Oliver_%28cropped%29.jpg")
    client.create_item(3, "GenbrugsPande", 2.75, 5, "Denne Pande er genbrugt og god for miljøet. God til vegansk mad","A","https://politiken.dk/imagevault/publishedmedia/4vnqctmr536aotcbtq58/combekk-pander3.jpg")
    client.create_item(4, "Selvvarmende Pande", 649.95, 5, "Denne Pande består af en lækker jern-legering, der bliver varm hvis man putter den i stikkontakten","A","https://pandasia.dk/wp-content/uploads/Produkter/Non-food/hot-pot-fondue.jpg.webp")
    client.create_item(5, "Støbejernspande", 649.95, 5, "Denne Pande består af en lækker jern-legering - den giver hård jern","A","https://www.kramogkanel.dk/wp-content/uploads/2020/01/1026569-Fiskars-Norden-cast-iron-frying-pan-26cm-1.jpg")
    client.create_item(6, "Panda", 1000000.99, 5, "Denne pande er lidt delikat, men af god kinesisk kvalitet","A","https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Giant_Panda_2004-03-2.jpg/1280px-Giant_Panda_2004-03-2.jpg")

    # Adding some basic users
    client.create_user(3)
    client.create_user(456)
    client.create_user( 789)

    app.run(debug=True, threaded=True)