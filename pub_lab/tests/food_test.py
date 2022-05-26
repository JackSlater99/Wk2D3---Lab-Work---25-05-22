import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Burger", 5, 3)

    def test_food_has_name(self):
        self.assertEqual("Burger", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(5, self.food.price)

    def test_food_has_rejuvination_level(self):
        self.assertEqual(3, self.food.rejuvination_level)