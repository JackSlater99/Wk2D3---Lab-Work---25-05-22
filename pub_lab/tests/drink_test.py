import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Vodka", 3, 1)
    def test_drink_has_name(self):
        self.assertEqual("Vodka", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(3, self.drink.price)

    def test_drink_has_alcohol_level(self):
        self.assertEqual(1, self.drink.alcohol_level)
