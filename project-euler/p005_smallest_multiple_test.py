import unittest

import p005_smallest_multiple as implementation


class SmallestMultipleTests(unittest.TestCase):
    def test_find_smallest_multiple(self):
        self.find_smallest_multiple_test(3, 6)
        self.find_smallest_multiple_test(4, 12)
        self.find_smallest_multiple_test(5, 60)

    def test_find_smallest_multiple_10(self):
        self.find_smallest_multiple_test(10, 2520)

    def test_find_smallest_multiple_20(self):
        self.find_smallest_multiple_test(20, 232792560)

    def find_smallest_multiple_test(self, value, expected_result):
        target = implementation.SmallestMultiple()
        result = target.find_smallest_multiple(value)
        self.assertEqual(expected_result, result)

    def test_is_multiple_to_all(self):
        self.is_multiple_to_all_test(2, 2, True)
        self.is_multiple_to_all_test(3, 6, True)
        self.is_multiple_to_all_test(4, 12, True)
        self.is_multiple_to_all_test(5, 60, True)
        self.is_multiple_to_all_test(3, 5, False)
        self.is_multiple_to_all_test(4, 10, False)
        self.is_multiple_to_all_test(5, 50, False)

    def is_multiple_to_all_test(self, max_multiplier, possible_multiple, expected_result):
        target = implementation.SmallestMultiple()
        result = target.is_multiple_to_all(max_multiplier, possible_multiple)
        self.assertEqual(expected_result, result)
 
    def test_is_multiple(self):
        self.is_multiple_test(2, 6, True)
        self.is_multiple_test(6, 12, True)
        self.is_multiple_test(3, 8, False)
        self.is_multiple_test(2, 89, False)

    def is_multiple_test(self, multiplier, possible_multiple, expected_result):
        target = implementation.SmallestMultiple()
        result = target.is_multiple(multiplier, possible_multiple)
        self.assertEqual(expected_result, result)

