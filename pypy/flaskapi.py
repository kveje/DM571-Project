from flask import Flask, jsonify, request
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
    

api.add_resource(Item, '/item')
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    instance = Instance()
    app.run(debug=True, threaded=True)