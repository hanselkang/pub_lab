import unittest
from src.pub import*
from src.customer import *
from src.drink import *
from src.food import *


class TestFood(unittest.TestCase):
    def setUp(self):
        self.food_1 = Food("Nachos", 9.99, 1)
        self.food_2 = Food("Hamburger", 12.99, 2)

        foods = [self.food_1, self.food_2]

    def test_food_name(self):
        self.assertEqual("Nachos",self.food_1.name)

    def test_food_price(self):
        self.assertEqual(12.99,self.food_2.price)

    def test_food_rejuvenation_level(self):
        self.assertEqual(1,self.food_1.rejuvenation_level)    