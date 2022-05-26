import unittest
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John Smith", 50, 21, 9)
        self.drink = Drink("Gin", 5, 3)
        self.food = Food("Fried Chicken", 10, 5)

    def test_customer_has_name(self):
        self.assertEqual("John Smith", self.customer.name)

    def test_wallet_has_money(self):
        self.assertEqual(50, self.customer.cash)

    # def test_customer_add_drink(self):
    #     self.customer.add_drink(self.drink)
    #     self.assertEqual(1, len(self.customer.drinks))

    def test_customer_can_reduce_cash(self):
        self.customer.reduce_cash(10)
        self.assertEqual(40, self.customer.cash)

    def test_customer_has_age(self):
        self.assertEqual(21, self.customer.age)

    def test_customer_has_drunkness_level(self):
        self.assertEqual(9, self.customer.drunkness_level)

    def test_customer_can_consume_drink(self):
        self.customer.consume_drink(self.drink)
        self.assertEqual(12, self.customer.drunkness_level)

    def test_customer_can_consume_drink(self):
        self.customer.consume_drink(self.drink)
        self.customer.consume_food(self.food)
        self.assertEqual(7, self.customer.drunkness_level)
