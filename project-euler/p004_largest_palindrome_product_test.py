import unittest

import p004_largest_palindrome_product as implementation


class LargestPalindromeProductTests(unittest.TestCase):
    def test_find_max_input_value(self):
        target = implementation.LargestPalindromeProduct()
        self.assertEqual(9, target.find_max_input_value(1))
        self.assertEqual(99, target.find_max_input_value(2))
        self.assertEqual(999, target.find_max_input_value(3))
    
    def test_1_digit_numbers(self):
        self.execute_test(1, 9)

    def test_2_digit_numbers(self):
        self.execute_test(2, 9009)

    def test_3_digit_numbers(self):
        self.execute_test(3, 906609)

    def test_4_digit_numbers(self):
        self.execute_test(4, 99000099)

    def execute_test(self, digit_count, expected_result):
        target = implementation.LargestPalindromeProduct()
        result = target.find_largest_palindrome_product(digit_count)
        self.assertEqual(expected_result, result)


class PalindromeCheckerTests(unittest.TestCase):
    def test_single_digit_numbers(self):
        for value in range(0, 10):
            self.execute_test(value, True)

    def test_double_digit_palindrome_numbers(self):
        for value in [11, 22, 33, 44, 55, 66, 77, 88, 99]:
            self.execute_test(value, True)

    def test_double_digit_non_palindrome_numbers(self):
        for value in [10, 12, 21, 23, 30, 98]:
            self.execute_test(value, False)

    def test_triple_digit_palindrome_numbers(self):
        for value in [111, 121, 272, 616, 999]:
            self.execute_test(value, True)
    
    def test_triple_digit_non_palindrome_numbers(self):
        for value in [100, 234, 543, 668, 998]:
            self.execute_test(value, False)

    def execute_test(self, value, expected_result):
        result = implementation.PalindromeChecker().is_palindrome(value)
        self.assertEqual(expected_result, result)


