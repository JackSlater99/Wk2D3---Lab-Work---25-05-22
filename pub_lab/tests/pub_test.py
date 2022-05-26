import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100)
        self.drink_1 = Drink("Vodka", 5, 1)
        self.drink_2 = Drink("Gin", 4, 2)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(50)
        self.assertEqual(150, self.pub.till)

    def test_sell_drink_to_customer(self):
        customer = Customer("Jack Jarvis", 100, 21)
        drink = Drink("Vodka", 5, 1)
        self.pub.sell_drink_to_customer(drink, customer)
        self.assertEqual(95, customer.cash)
        self.assertEqual(105, self.pub.till)
        self.assertEqual(1, customer.drunkness_level)
        # self.assertEqual(1, len(customer.drinks))

    def test_sell_drink_to_underage_customer(self):
        customer = Customer("James Allan", 40, 17)
        drink = Drink("Vodka", 5, 1)
        sale = self.pub.sell_drink_to_customer(drink, customer)
        self.assertEqual(False, sale)

    def test_sell_drink_to_drunk_customer(self):
        customer = Customer("James Allan", 40, 19, 10)
        drink = Drink("Vodka", 5, 1)
        sale = self.pub.sell_drink_to_customer(drink, customer)
        self.assertEqual(False, sale)

    def test_sell_food_to_drunk_customer(self):
        customer = Customer("James Allan", 100, 15, 10)
        food = Food("Chips", 2, 2)
        self.pub.sell_food_to_customer(food, customer)
        self.assertEqual(98, customer.cash)
        self.assertEqual(102, self.pub.till)
        self.assertEqual(8, customer.drunkness_level)

    def test_pub_has_stock(self):
        self.pub.add_drink_to_stock(self.drink_1)
        self.assertEqual(1, self.pub.drinks[self.drink_1.name]["quantity"])
        self.pub.add_drink_to_stock(self.drink_1)
        self.assertEqual(2, self.pub.drinks[self.drink_1.name]["quantity"])
        self.pub.add_drink_to_stock(self.drink_2)
        self.assertEqual(1, self.pub.drinks[self.drink_2.name]["quantity"])       
        breakpoint()

    # def test_check_total_value(self):
    #     self.pub.add_drink_to_stock(self.drink_1)
    #     self.pub.add_drink_to_stock(self.drink_2)
    #     self.pub.add_drink_to_stock(self.drink_2)
    #     stock = self.pub.stock_value()
    #     self.assertEqual(9, stock)