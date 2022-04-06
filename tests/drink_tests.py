import unittest
from src.pub import*
from src.customers import *
from src.drinks import *


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Edinburgh Gin", 3.90, 2)

    # @unittest.skip("-")
    def test_find_drink_name(self):
        self.assertEqual("Edinburgh Gin", self.drink.name)

    def test_drink_price(self):
        self.assertEqual(3.90,self.drink.price)
