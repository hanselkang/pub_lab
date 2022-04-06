import unittest
from src.pub import *
from src.customers import *
from src.drinks import *


class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drinks("Edinburgh Gin", 3.90)
        self.drink_2 = Drinks("Tennent's", 3.20)

        drinks = [self.drink_1, self.drink_2]
        
        self.pub = Pub("King's Arm", 1000.00, drinks)
        


    def test_pub_name(self):
        self.assertEqual("King's Arm", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(1000.00, self.pub.till)

    def test_buy_drink(self):
        customer = Customers("David", 50.00)
        self.pub.buy_a_drink("Edinburgh Gin",customer)

        self.assertEqual(1003.90, self.pub.till)
        self.assertEqual(46.10, customer.wallet)
