import unittest
from solution_1 import get_min_price
class TestCheapestOperator(unittest.TestCase):
    def test_no_matching_prefix(self):
        number = "9876543210"
        price_lists = [ {"1": 0.9, "46": 0.17}, {"44": 0.5, "48": 1.2}]
        cheapest_operator, cheapest_price = get_min_price(number, price_lists)
        self.assertIsNone(cheapest_operator)
        self.assertEqual(cheapest_price, float('inf'))

    def test_matching_prefix(self):
        number = "4620123456"
        price_lists = [{"1": 0.9, "46": 0.17, "4620": 0.0},{"44": 0.5, "48": 1.2}]
        cheapest_operator, cheapest_price = get_min_price(number, price_lists)
        self.assertEqual(cheapest_operator, 0)
        self.assertEqual(cheapest_price, 0.0)
    def test_with_empty_operators(self):
        number = "4620123456"
        price_lists = []
        cheapest_operator, cheapest_price = get_min_price(number, price_lists)
        self.assertIsNone(cheapest_operator)
        self.assertEqual(cheapest_price,float('inf'))
    def test_duplicate_prefixes(self):
        number = "4684620123456"
        price_lists = [{"1": 0.9, "46": 0.17, "468": 0.1, "4681": 0.2}]
        cheapest_operator, cheapest_price = get_min_price(number, price_lists)
        self.assertEqual(cheapest_operator, 0)
        self.assertEqual(cheapest_price, 0.1)



unittest.main(verbosity=2)