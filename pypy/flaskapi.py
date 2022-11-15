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
        lst = client.get_user_list()
        print(request.headers)
        print(lst)
        if request.headers.get('Authorization') == AUTH:
           print("GODKENT!")
           return jsonify(client.get_user_list())
        else:
           return "", 400

class User(Resource):
    def post(self):
        print(request.headers)
        print(request.get_json())
        print(request.headers['Content-type'])
        request_json = request.get_json()
        
        if request.headers.get('Authorization') == AUTH:
            try:
                client.create_user(request_json["user_id"])
                return "", 201   
            except:
                return "Wah wah waaaaaah, bad request", 400
        else:
           return "Unauthorized", 401

class Basket(Resource):
    def get(self, user_id):
        if request.headers.get('Authorization') == AUTH:
            if user_id not in client.get_user_list():
                return "No user with id", 400
            elif not hasattr(client.get_user(user_id), 'shopping_basket'):
                return "User doesn\'t have a basket", 400
            else:
                try:
                    user = client.get_user(user_id)   
                    item_list = client.get_basket_items(user.shopping_basket)
                    return make_response(jsonify(item_list), 200)
                except:
                    return "Bad request", 400
        else:
            return "Unauthorized", 401
    
    def post(self, user_id):
        if request.headers.get('Authorization') == AUTH:
            if user_id not in client.get_user_list():
                return "No user with id", 400
            elif hasattr(client.get_user(user_id), 'shopping_basket'):
                return "User already has a basket", 400
            else:
                try:
                    client.create_shopping_basket(client.get_user(user_id))
                    print(client.get_user(user_id).shopping_basket)
                    return "", 201
                except:
                    return "Bad request", 400
        else:
            return "Unauthorized", 401
    
    def put(self, user_id):
        req = request.get_json()
        if request.headers.get('Authorization') == AUTH:
            if user_id not in client.get_user_list():
                return "No user with id", 400
            elif not hasattr(client.get_user(user_id), 'shopping_basket'):
                return "User doesn\'t have a basket", 400
            else:
                try:
                    user = client.get_user(user_id)
                    item = client.get_item(req['item_id'])
                    user.shopping_basket.update(item, req['item_amount'])
                    return "", 200
                except:
                    return "Bad request", 400
        else:
            return "Unauthorized", 401


"""INGEN CHECK OVERHOVEDET I FØLGENDE CLASSES, BARE FOR AT FÅ ET ELLER ANDET NED"""
class Order(Resource):
    def get(self, user_id):
        return make_response(jsonify(client.get_basket_items(client.orders[user_id])), 200)
        
    def post(self, user_id):
        user = client.get_user(user_id)
        client.create_order(user)
        return "", 201

class Orders(Resource):
    def get(self):
        orders_list = []
        for order in client.orders.values():
            orders_list.append(client.get_basket_items(order))
        
        return make_response(jsonify(orders_list), 200)
        
        # En dict hvis der menes at man skal kunne se hvilket id til hvilken order
        # Og vi ikke gør at index i den her order liste er = order id, som der gøres oven over
        
        # for id, order in client.orders.items():
        #     client.orders[id] = client.get_basket_items(order)
        
        # return make_response(jsonify(client.orders), 200)
        
class Inventory(Resource):
    def get(self):
        inventory_list = client.get_inventory()
        return {"data" : inventory_list}, 200
    
    def post(self):
        req = request.get_json()
        if request.headers.get('Authorization') == AUTH:
            if req['id'] in client.inventory.items:
                return "Item already exists", 400
            else:
                #100p en nemmere mmåde at gøre det her på bare en quick fix lige nu
                client.create_item(req['id'], req['name'], req['price'],req['stock_lvl_local'],req['description'],req['supplier'],req['photo_url'])
                return "", 201
        else:
           return "", 400

api.add_resource(UserList, '/user-list')
api.add_resource(User, '/user')
api.add_resource(Basket, '/user/<int:user_id>/basket')
api.add_resource(Order, '/user/<int:user_id>/order')
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
    
    app.run(debug=True, threaded=True)