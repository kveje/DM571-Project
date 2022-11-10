from item import Item

class Inventory(Item):
    def __init__(self):
        self.items = {}
        
    def add(self, item:Item):
        self.items[item.id] = item
        
    def remove(self, id):
        self.items.pop(id)

    def update_stock_lvl(self, id: int, qty: int):
        self.items[id].set_stock_lvl_local = qty

if __name__ == "__main__":
    inv = Inventory()
    inv.add(Item(1, "Wok", 20.0, 5, "Den Ægte Pande. Approved af det ægte karryfarvede folk!", "A","https://cdn.shopify.com/s/files/1/2807/7652/products/Nexgrill_Pro_Wok_website.png?v=1559905032"))
    inv.add(Item(2, "Jamie Oliver", 189.95, 5, "Han laver mad på pander og fik skæld ud af en gonger fordi han ikke stegte gode ris","A","https://upload.wikimedia.org/wikipedia/commons/3/38/Jamie_Oliver_%28cropped%29.jpg"))
    inv.add(Item(3, "GenbrugsPande", 2.75, 5, "Denne Pande er genbrugt og god for miljøet. God til vegansk mad","A","https://politiken.dk/imagevault/publishedmedia/4vnqctmr536aotcbtq58/combekk-pander3.jpg"))
    inv.add(Item(4, "Selvvarmende Pande", 649.95, 5, "Denne Pande består af en lækker jern-legering, der bliver varm hvis man putter den i stikkontakten","A","https://pandasia.dk/wp-content/uploads/Produkter/Non-food/hot-pot-fondue.jpg.webp"))
    inv.add(Item(5, "Støbejernspande", 649.95, 5, "Denne Pande består af en lækker jern-legering - den giver hård jern","A","https://www.kramogkanel.dk/wp-content/uploads/2020/01/1026569-Fiskars-Norden-cast-iron-frying-pan-26cm-1.jpg"))
    inv.add(Item(6, "Panda", 1000000.99, 5, "Denne pande er lidt delikat, men af god kinesisk kvalitet","A","https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Giant_Panda_2004-03-2.jpg/1280px-Giant_Panda_2004-03-2.jpg"))
