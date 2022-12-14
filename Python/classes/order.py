from classes.basket import Basket
from classes.item import Item
from classes.user import User


class Order:
    """Object representing an order"""

    def __init__(self, user: User):
        item_list = []
        for item in user.basket.basket.keys():
            amount = user.basket.basket[item]
            item.inc_stock_lvl_local(-amount)
            item_dict = item.get_item()
            item_dict["amount"] = amount
            item_list.append(item_dict)
        self.order = {
            "uid": user.uid,
            "items": item_list,
        }
