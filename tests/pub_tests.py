import unittest
from src.pub import*
from src.customers import *
from src.drinks import *


class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("King's Arm", 1000.00)
        self.drink = Drinks("Edinburgh Gin", 3.90)
        self.customer = Customers("David", 50.00)

    def test_buy_drink(self):
        self.assertEqual(1003.90, self.pub.buy_a_drink())