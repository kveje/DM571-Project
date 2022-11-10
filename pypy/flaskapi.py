from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api
from instance import Instance

app = Flask(__name__)
api = Api(app)

TEST_ITEM = {
    "id": 1,
    "name": "Pande",
    "price": 20.0,
    "description": "vn",
    "photo_url": "hhtp",
    "stock_lvl_local": 5,
    "stock_lvl_supplier": 0,
    "supplier": "kk"
}

class HelloWorld(Resource):
    def get(self):
        print(request.json)
        a= request.json
        return instance.hello()
    
class Item(Resource):
    def get(self):
        return jsonify(TEST_ITEM)
    
    def post(self):
        return jsonify(TEST_ITEM)
    
class UserList(Resource):
    def get(self):
        lst = instance.get_user_list()
        obj = {
          1: "Hej",
          2: "OGSÅ",
          3: "ÆALSDLAÆSKDÆ"
        }
        return obj
        #if request.headers.get('Authorization') == "123456789":
        #    print("GODKENT!")
        #    return jsonify(instance.get_user_list()), 200
        #else:
        #    return "Nej nej nej", 400

class User(Resource):
    def post(self):
        request_json = request.get_json(force=True)
        try:
           instance.create_user(request_json["user_id"])
           return "", 200
        except:
            return "", 401
        

api.add_resource(Item, '/item')
api.add_resource(HelloWorld, '/')
api.add_resource(UserList, '/user-list')
api.add_resource(User, '/user')

if __name__ == '__main__':
    instance = Instance()
    app.run(debug=True, threaded=True)