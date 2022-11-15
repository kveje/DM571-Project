from flask import Flask, jsonify, request, make_response, json
from flask_restful import Resource, Api
from instance import Instance

app = Flask(__name__)
api = Api(app)

AUTH = "123456789"
    
class Item(Resource):
    def post(self):
        req = request.get_json()
        if request.headers.get('Authorization') == AUTH:
            if req['id'] in instance.inventory.items:
                return "Item already exists", 400
            else:
                #100p en nemmere mmåde at gøre det her på bare en quick fix lige nu
                instance.create_item(req['id'], req['name'], req['price'],req['stock_lvl_local'],req['description'],req['supplier'],req['photo_url'])
                return "", 201
        else:
           return "", 400
    
class UserList(Resource):
    def get(self):
        lst = instance.get_user_list()
        print(request.headers)
        print(lst)
        if request.headers.get('Authorization') == AUTH:
           print("GODKENT!")
           return jsonify(instance.get_user_list())
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
                instance.create_user(request_json["user_id"])
                return "", 201   
            except:
                return "Wah wah waaaaaah, bad request", 400
        else:
           return "Unauthorized", 401

class Basket(Resource):
    def get(self, user_id):
        if request.headers.get('Authorization') == AUTH:
            if user_id not in instance.get_user_list():
                return "No user with id", 400
            elif not hasattr(instance.get_user(user_id), 'shopping_basket'):
                return "User doesn\'t have a basket", 400
            else:
                try:
                    user = instance.get_user(user_id)   
                    item_list = instance.get_basket_items(user.shopping_basket)
                    return make_response(jsonify(item_list), 200)
                except:
                    return "Bad request", 400
        else:
            return "Unauthorized", 401
    
    def post(self, user_id):
        if request.headers.get('Authorization') == AUTH:
            if user_id not in instance.get_user_list():
                return "No user with id", 400
            elif hasattr(instance.get_user(user_id), 'shopping_basket'):
                return "User already has a basket", 400
            else:
                try:
                    instance.create_shopping_basket(instance.get_user(user_id))
                    print(instance.get_user(user_id).shopping_basket)
                    return "", 201
                except:
                    return "Bad request", 400
        else:
            return "Unauthorized", 401
    
    def put(self, user_id):
        req = request.get_json()
        if request.headers.get('Authorization') == AUTH:
            if user_id not in instance.get_user_list():
                return "No user with id", 400
            elif not hasattr(instance.get_user(user_id), 'shopping_basket'):
                return "User doesn\'t have a basket", 400
            else:
                try:
                    user = instance.get_user(user_id)
                    item = instance.get_item(req['item_id'])
                    user.shopping_basket.update(item, req['item_amount'])
                    return "", 200
                except:
                    return "Bad request", 400
        else:
            return "Unauthorized", 401


"""INGEN CHECK OVERHOVEDET I FØLGENDE CLASSES, BARE FOR AT FÅ ET ELLER ANDET NED"""
class Order(Resource):
    def get(self, user_id):
        return make_response(jsonify(instance.get_basket_items(instance.orders[user_id])), 200)
        
    def post(self, user_id):
        user = instance.get_user(user_id)
        instance.create_order(user)
        return "", 201

class Orders(Resource):
    def get(self):
        orders_list = []
        for order in instance.orders.values():
            orders_list.append(instance.get_basket_items(order))
        
        return make_response(jsonify(orders_list), 200)
        
        # En dict hvis der menes at man skal kunne se hvilket id til hvilken order
        # Og vi ikke gør at index i den her order liste er = order id, som der gøres oven over
        
        # for id, order in instance.orders.items():
        #     instance.orders[id] = instance.get_basket_items(order)
        
        # return make_response(jsonify(instance.orders), 200)
        
        

api.add_resource(Item, '/item')
api.add_resource(UserList, '/user-list')
api.add_resource(User, '/user')
api.add_resource(Basket, '/user/<int:user_id>/basket')
api.add_resource(Order, '/user/<int:user_id>/order')
api.add_resource(Orders, '/orders')


if __name__ == '__main__':
    instance = Instance()
    app.run(debug=True, threaded=True)