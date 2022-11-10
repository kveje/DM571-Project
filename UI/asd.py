from flask import Flask, Request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        dict1 = {'hello':'world'}
        return dict1

    def post(self):
        return '',200

class InventoryHandler(Resource):    
    def get(self):
        return ''


api.add_resource(HelloWorld, '/hello')
api.add_resource(InventoryHandler, '/inventory')

if __name__ == '__main__':
    app.run(debug=True)