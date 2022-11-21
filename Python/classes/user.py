from classes.basket import Basket


class User():
    """Object representing a user"""

    def __init__(self, uid: int, name: str, password: str, mail: str):
        self.uid = uid
        self.name = name
        self.password = password
        self.mail = mail

    def create_basket(self, basket: Basket) -> None:
        """Creates a shoppingbasket for the given user"""
        self.basket = basket

    def remove_basket(self) -> None:
        delattr(self, "basket")
