import unittest
from src.pub import *
from src.customers import *
from src.drinks import *


class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Edinburgh Gin", 3.90)
        self.drink_2 = Drink("Tennent's", 3.20)

        drinks = [self.drink_1, self.drink_2]
        
        self.pub = Pub("King's Arm", 1000.00, drinks)
        self.customer_1 = Customer("David", 50.00, 30)
        self.customer_2 = Customer("Anna", 10.00, 17)


    def test_pub_name(self):
        self.assertEqual("King's Arm", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(1000.00, self.pub.till)

    def test_buy_drink(self):
        
        self.pub.buy_a_drink("Edinburgh Gin",self.customer_1)

        self.assertEqual(1003.90, self.pub.till)
        self.assertEqual(46.10, self.customer_1.wallet)

    def test_can_drink(self):
        self.assertEqual(True, self.pub.can_drink(self.customer_1.age))
