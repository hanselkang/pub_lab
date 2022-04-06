import unittest
from src.pub import*
from src.customers import *
from src.drinks import *

class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer = Customers("David",50.00)