def get_stock_lvl_supplier_A(id:int) -> int:
    """Function for communicating with Supplier A's API"""
    if id < 3:
        return 5
    else:
        return 10

def get_stock_lvl_supplier_B(id:int) -> int:
    """Function for communicating with Supplier B's API"""
    if id > 3:
        return 5
    else:
        return 10

class Item():
    """Item class, that handles item stuff"""
    def __init__(self, id: int, name: str, price: int, stock_lvl_local: int, description: str, supplier: str, photo_url: str):
        self.id = id
        self.name = name
        self.price = price
        self.stock_lvl_local = stock_lvl_local
        self.description = description
        self.supplier = supplier
        self.photo_url = photo_url
    
    def get_supplier_lvl(self):
        """Returns the updated item information in a dict"""
        if self.supplier == "A" or self.supplier == "a":
            return get_stock_lvl_supplier_A(self.id)
        elif self.supplier == "B":
            return get_stock_lvl_supplier_B(self.id)
        else:
            return KeyError
    
    def get_item(self):
        """Returns the updated item information in a dict"""
        stock_lvl_supplier = self.get_supplier_lvl()
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock_lvl_local': self.stock_lvl_local,
            'stock_lvl_supplier': stock_lvl_supplier,
            'description': self.description,
            'supplier': self.supplier,
            'photo_url': self.photo_url
        }
    
    def set_stock_lvl_local(self, qty: int):
        """Setter for local stock level value"""
        self.stock_lvl_local = qty