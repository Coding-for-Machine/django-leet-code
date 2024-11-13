from unittest_user import def linear_search(arr, target):
import unittest

class TestLinearSearch(unittest.TestCase):
    def test_found(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(linear_search(['a', 'b', 'c'], 'b'), 1)

    def test_not_found(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(linear_search(['a', 'b', 'c'], 'd'), -1)

    def test_empty_list(self):
        self.assertEqual(linear_search([], 1), -1)

    def test_first_element(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 1), 0)

    def test_last_element(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 5), 4)

if __name__ == '__main__':
    unittest.main()