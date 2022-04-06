import unittest
from src.pub import*
from src.customer import *
from src.drink import *
from src.food import *


class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Edinburgh Gin", 3.90, 2)
        self.drink_2 = Drink("Tennent's", 3.20, 1)

        drinks = [self.drink_1, self.drink_2]

        self.food_1 = Food("Nachos", 9.99, 1)
        self.food_2 = Food("Hamburger", 12.99, 2)

        foods = [self.food_1, self.food_2]

        self.pub = Pub("King's Arm", 1000.00, drinks, foods)
        self.customer_1 = Customer("David", 50.00, 30)
        self.customer_2 = Customer("Anna", 10.00, 17)

    def test_pub_name(self):
        self.assertEqual("King's Arm", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(1000.00, self.pub.till)

    def test_can_drink(self):
        self.assertEqual(True, self.pub.can_drink(self.customer_1))

    def test_can_drink(self):
        self.assertEqual(False, self.pub.can_drink(self.customer_2))

    def test_drunkenness_check(self):
        self.assertEqual(True, self.pub.check_drunkenness(self.customer_1))

    def test_drunkenness_check(self):
        self.customer_1.drunkenness = 6
        self.assertEqual(False, self.pub.check_drunkenness(self.customer_1))

    def test_buy_drink(self):

        self.pub.buy_a_drink("Edinburgh Gin", self.customer_1)

        self.assertEqual(1003.90, self.pub.till)
        self.assertEqual(46.10, self.customer_1.wallet)
        self.assertEqual(2, self.customer_1.drunkenness)

    def test_buy_food(self):
        self.customer_1.drunkenness = 4
        self.pub.buy_food("Nachos", self.customer_1)
        self.assertEqual(1009.99, self.pub.till)
        self.assertEqual(40.01, self.customer_1.wallet)
        self.assertEqual(3, self.customer_1.drunkenness)
