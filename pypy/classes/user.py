class User:
    def __init__(self, id):
        self.id = id
    
    def create_shopping_basket(self, shopping_basket):
        self.shopping_basket = shopping_basket
    
    def get_user_json(self):
        return self.id