import unittest
from src.pub import*
from src.customers import *
from src.drinks import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customers("David",50.00)

    def test_customer_has_name(self):
        self.assertEqual("David",self.customer.name)

    def test_customer_has_money(self):
        self.assertEqual(50.00,self.customer.wallet)