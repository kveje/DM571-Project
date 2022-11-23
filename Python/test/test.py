import unittest
import io

# For relative imports to work
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.basket import Basket
from classes.item import Item
from classes.user import User

""""
How to get coverage:

Got to \DM571-Project\Python

Then run tests:
python -m coverage run -m unittest -v

Get coverage:
python -m coverage report 

Get html:
python -m coverage html

"""


class ItemTest(unittest.TestCase):
    def setUp(self):
        self.item = Item(1, "Wok", 20.0, 15, "Pande", "A", "https")

        self.item2 = Item(1, "Wok", 20.0, 15, "Pande", "B", "https")

    def test_create_item(self):
        """Create an item"""
        self.assertEqual(self.item.id, 1)
        self.assertEqual(self.item.name, "Wok")
        self.assertEqual(self.item.price, 20.0)
        self.assertEqual(self.item.stock_lvl_local, 15)
        self.assertEqual(self.item.description, "Pande")
        self.assertEqual(self.item.supplier, "A")
        self.assertEqual(self.item.photo_url, "https")

    def test_get_item_dict_A(self):
        """Get the dict representation of an item"""
        item_dict = self.item.get_item()
        expected_dict = {
            "id": 1,
            "name": "Wok",
            "price": 20.0,
            "stock_lvl_local": 15,
            "stock_lvl_supplier": 20,
            "description": "Pande",
            "supplier": "A",
            "photo_url": "https",
        }

        self.assertDictEqual(item_dict, expected_dict)

    def test_get_item_dict_B(self):
        """Get the dict representation of an item"""
        item_dict = self.item2.get_item()
        expected_dict = {
            "id": 1,
            "name": "Wok",
            "price": 20.0,
            "stock_lvl_local": 15,
            "stock_lvl_supplier": 20,
            "description": "Pande",
            "supplier": "B",
            "photo_url": "https",
        }

        self.assertDictEqual(item_dict, expected_dict)

    def test_get_local_stock_lvl(self):
        """Get local stock lvl"""
        self.assertEqual(self.item.get_stock_lvl_local(), 15)

    def test_local_stock_lvl_inc(self):
        """Increment the local stock level with a given amount"""
        self.item.inc_stock_lvl_local(3)
        self.assertEqual(self.item.stock_lvl_local, 15 + 3)


class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User(123, "Carsten", "Lkj/62dfg", "carsten@email.dk")
        self.user.create_basket(Basket())

        self.user1 = User(456, "Kasper", "LIhs752ns", "kasper@email.dk")

    def test_user_creation(self):
        """User creation"""
        self.assertEqual(self.user.uid, 123)
        self.assertEqual(self.user.name, "Carsten")
        self.assertEqual(self.user.password, "Lkj/62dfg")
        self.assertEqual(self.user.mail, "carsten@email.dk")

    def test_basket(self):
        """reation of a user's basket"""
        self.assertTrue(hasattr(self.user, "basket"))

    def test_basket2(self):
        """Test that a basket hasn't been created, before create_basket()"""
        self.assertFalse(hasattr(self.user1, "basket"))

    def test_remove_basket(self):
        """Removal of a user's basket"""
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
            "Pande",
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
            0,
            "Denne Pande består af en lækker jern-legering, der bliver varm hvis man putter den i stikkontakten",
            "A",
            "https://pandasia.dk/wp-content/uploads/Produkter/Non-food/hot-pot-fondue.jpg.webp",
        )

    def test_update_success(self):
        """Successfull update item in a basket"""
        self.basket.update(self.item1, 5)
        self.assertIn(self.item1, self.basket.basket)
        self.assertEqual(len(self.basket.basket), 1)
        self.assertEqual(self.basket.basket[self.item1], 5)

    def test_update_item_not_in_basket(self):
        """Check that an item hasn't been added by mistake"""
        self.basket.update(self.item1, 5)
        self.assertNotIn(self.item2, self.basket.basket)
        self.assertEqual(len(self.basket.basket), 1)
        self.assertEqual(self.basket.basket[self.item1], 5)

    def test_update_not_in_stock(self):
        """Try to update an item but amount is more than stock level"""
        capture_response = io.StringIO()  # Create StringIO object
        sys.stdout = capture_response  # Redirect stdout.
        self.basket.update(self.item1, 20)  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual(capture_response.getvalue(), "Only 15 Wok(s) in inventory\n")

    def test_update_not_in_inventory(self):
        """Try to update an item that isn't in the inventory"""
        capture_response = io.StringIO()
        sys.stdout = capture_response
        self.basket.update(self.item4, 5)
        sys.stdout = sys.__stdout__
        self.assertEqual(capture_response.getvalue(), "Not in inventory\n")

    def test_update_negative_amount(self):
        """Try to update an item with a negative amount"""
        capture_response = io.StringIO()
        sys.stdout = capture_response
        self.basket.update(self.item1, -5)
        sys.stdout = sys.__stdout__
        self.assertEqual(capture_response.getvalue(), "Must be a positive amount\n")

    def test_remove_success(self):
        """Succesfull removal of item from the cart"""
        self.basket.update(self.item1, 5)
        self.assertIn(self.item1, self.basket.basket)
        self.assertEqual(len(self.basket.basket), 1)
        self.assertEqual(self.basket.basket[self.item1], 5)

        self.basket.remove(self.item1)
        self.assertNotIn(self.item1, self.basket.basket)
        self.assertEqual(len(self.basket.basket), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
