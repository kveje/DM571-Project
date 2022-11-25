### THE FOUR HANDLERS SHOULD BE PLACED SOMEWHERE ELSE FOR PRODUCTION
def get_stock_lvl_supplier_A(id: int) -> int:
    """Function for communicating with Supplier A's API"""
    # Here should be some logic for calling the supplier API
    if id < 3:
        return 20
    else:
        return 10


def get_stock_lvl_supplier_B(id: int) -> int:
    """Function for communicating with Supplier B's API"""
    # Here should be some logic for calling the supplier API
    if id > 3:
        return 10
    else:
        return 20


def order_from_supplier_A(id: int, amount: int) -> int:
    """Function for ordering from supplier B"""
    stock_lvl_supplier = get_stock_lvl_supplier_A(id)
    if amount > stock_lvl_supplier:
        # Some logic for ordering from supplier
        return stock_lvl_supplier
    else:
        # Some logic for ordering from supplier
        return amount


def order_from_supplier_B(id: int, amount: int) -> int:
    """Function for ordering from supplier B"""
    stock_lvl_supplier = get_stock_lvl_supplier_B(id)
    if amount > stock_lvl_supplier:
        # Some logic for ordering from supplier
        return stock_lvl_supplier
    else:
        # Some logic for ordering from supplier
        return amount


class Item:
    """Item class, that handles item stuff"""

    def __init__(
        self, id: int, name: str, price: int, stock_lvl_local: int, description: str, supplier: str, photo_url: str
    ):
        self.id = id
        self.name = name
        self.price = price
        self.stock_lvl_local = stock_lvl_local
        self.description = description
        self.supplier = supplier
        self.photo_url = photo_url

    def get_supplier_lvl(self) -> int:
        """Returns the updated item information in a dict"""
        if self.supplier == "A" or self.supplier == "a":
            return get_stock_lvl_supplier_A(self.id)
        elif self.supplier == "B" or self.supplier == "b":
            return get_stock_lvl_supplier_B(self.id)

    def get_item(self) -> dict:
        """Returns the updated item information in a dict"""
        stock_lvl_supplier = self.get_supplier_lvl()
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock_lvl_local": self.stock_lvl_local,
            "stock_lvl_supplier": stock_lvl_supplier,
            "description": self.description,
            "supplier": self.supplier,
            "photo_url": self.photo_url,
        }

    def get_stock_lvl_local(self) -> int:
        """Getter for local stock level value"""
        return self.stock_lvl_local

    def inc_stock_lvl_local(self, inc: int) -> None:
        """Setter for local stock level value"""
        self.stock_lvl_local += inc

    def order_from_supplier(self, amount) -> None:
        """Orders an amount of the item from the supplier"""
        if self.supplier == "A" or self.supplier == "a":
            ordered_amount = order_from_supplier_A(self.id, amount)
            self.stock_lvl_local += ordered_amount
        elif self.supplier == "B" or self.supplier == "b":
            ordered_amount = order_from_supplier_B(self.id, amount)
            self.stock_lvl_local += ordered_amount
