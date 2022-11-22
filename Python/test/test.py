import unittest

# For relative imports to work
import sys, os; sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.basket import Basket
from classes.item import Item
from classes.user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User(123, "Carsten", "Lkj/62dfg", "carsten@email.dk")
        self.user.create_basket(Basket())
        
    def test_user_creation(self):
        """Test user creation"""
        self.assertEqual(self.user.uid, 123)
        self.assertEqual(self.user.name, "Carsten")
        self.assertEqual(self.user.password, "Lkj/62dfg")
        self.assertEqual(self.user.mail, "carsten@email.dk")
    
    def test_basket(self):
        """Test creation of a user's basket"""
        self.assertTrue(hasattr(self.user, "basket"))
        
    def test_remove_basket(self):
        """Test removal of a user's basket"""
        self.user.remove_basket()
        self.assertFalse(hasattr(self.user, "basket"))

class BasketTest(unittest.TestCase):
    def setUp(self):
        self.basket = Basket()
        self.item1 = Item(
                            1,
                            "Wok",
                            20.0,
                            15,
                            "Den Ægte Pande. Approved af det ægte karryfarvede folk!",
                            "A",
                            "https://cdn.shopify.com/s/files/1/2807/7652/products/Nexgrill_Pro_Wok_website.png?v=1559905032",
                        )
        self.item2 = Item(
                            2,
                            "Jamie Oliver",
                            189.95,
                            10,
                            "Han laver mad på pander og fik skæld ud af en gonger fordi han ikke stegte gode ris",
                            "A",
                            "https://upload.wikimedia.org/wikipedia/commons/3/38/Jamie_Oliver_%28cropped%29.jpg",
                        )
        self.item3 = Item(
                            3,
                            "GenbrugsPande",
                            2.75,
                            12,
                            "Denne Pande er genbrugt og god for miljøet. God til vegansk mad",
                            "A",
                            "https://politiken.dk/imagevault/publishedmedia/4vnqctmr536aotcbtq58/combekk-pander3.jpg",
                        )
        self.item4 = Item(
                            4,
                            "Selvvarmende Pande",
                            649.95,
                            16,
                            "Denne Pande består af en lækker jern-legering, der bliver varm hvis man putter den i stikkontakten",
                            "A",
                            "https://pandasia.dk/wp-content/uploads/Produkter/Non-food/hot-pot-fondue.jpg.webp"
                        )
        
    def test_update_success(self):
        self.basket.update(self.item1, 5)
        self.assertIn(self.item1, self.basket.basket)
        self.assertTrue(len(self.basket.basket), 1)
        self.assertEqual(self.basket.basket[self.item1], 5)
    
    def test_update_item_not_in_basket(self):
        self.basket.update(self.item1, 5)
        self.assertNotIn(self.item2, self.basket.basket)
        self.assertEqual(self.basket.basket[self.item1], 5)
    
    def test_update_not_in_stock(self):
        self.assertTrue(str(self.basket.update(self.item1, 20)), "Only 15 Wok(s) in inventory")
        
    
    def test_remove_success(self):
        pass
        
if __name__ == '__main__':
    unittest.main(verbosity=2)