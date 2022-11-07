from unicodedata import name


class Item:
    def __init__(self, id, name, type, price, stock, description, supplier, picture): #Kører vi uden gettere og setter her?
        self.id = id
        self.name = name
        self.type = type
        self.price = price
        self.stock = stock
        self.description = description
        self.supplier = supplier
        self.picture = picture