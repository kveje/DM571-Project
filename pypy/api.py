from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from flask_restful import Resource, Api
from client import Client

app = Flask(__name__)
CORS(app)
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
    
class Item(Resource):
    def get(self):

        return jsonify(TEST_ITEM)
    
    def post(self):
        return jsonify(TEST_ITEM)
    
class UserList(Resource):
    def get(self):
        lst = client.get_user_list()
        print(lst)
        return { "data" : lst}, 200
        #if request.headers.get('Authorization') == "123456789":
        #    print("GODKENT!")
        #    return jsonify(instance.get_user_list()), 200
        #else:
        #    return "Nej nej nej", 400

class User(Resource):
    def post(self):
        request_json = request.get_json(force=True)
        try:
           client.create_user(request_json["user_id"])
           return "", 200
        except:
            return "", 401

class Inventory(Resource):
    def get(self):
        inventory_list = client.get_inventory()
        return {"data" : inventory_list}, 200
        

api.add_resource(Item, '/item')
api.add_resource(UserList, '/user-list')
api.add_resource(User, '/user')
api.add_resource(Inventory,'/inventory')

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