import unittest
from src.pub import *
from src.customer import *
from src.drink import *
from src.food import *


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("David", 50.00, 30)

    def test_customer_has_name(self):
        self.assertEqual("David", self.customer.name)

    def test_customer_has_money(self):
        self.assertEqual(50.00, self.customer.wallet)

    def test_customer_age(self):
        self.assertEqual(30, self.customer.age)
