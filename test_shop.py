import unittest
from shop_homework4 import *

class TestMyShop(unittest.TestCase):

    def test_greet_customer(self):
        self.assertEqual(greet_customer(), "All is ok")

    def test_display_item(self):
        stock = {
            "Speaker": 80,
            "Laptop": 150,
            "DVD player": 60
        }
        self.assertEqual(display_items(stock), "All is ok")

    def test_select_item(self):
        self.assertEqual(select_item(), "All is ok")


