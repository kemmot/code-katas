import unittest

import p002_even_fibonacci_numbers as implementation


class ImplementationTests(unittest.TestCase):
    def setUp(self):
        self.target = implementation.EvenFibonacciNumbers()
    
    def test_sum_to_1_is_0(self):
        self.execute_test(1, 0)

    def test_sum_to_2_is_2(self):
        self.execute_test(2, 2)
    
    def test_sum_to_7_is_2(self):
        self.execute_test(7, 2)
    
    def test_sum_to_8_is_10(self):
        self.execute_test(8, 10)
    
    def test_sum_to_33_is_10(self):
        self.execute_test(33, 10)
    
    def test_sum_to_34_is_44(self):
        self.execute_test(34, 44)
    
    def test_sum_to_4m(self):
        self.execute_test(4000000, 4613732)
    
    def execute_test(self, max, expected_result):
        result = self.target.execute(max)
        self.assertEqual(expected_result, result)

class FibonacciGeneratorTests(unittest.TestCase):
    def setUp(self):
        self.target = implementation.FibonacciGenerator()
    
    def test_get_fibonacci_max_0(self):
        self.execute_test(0, [])

    def test_get_fibonacci_max_1(self):
        self.execute_test(1, [1])

    def test_get_fibonacci_max_2(self):
        self.execute_test(2, [1,2])

    def test_get_fibonacci_max_3(self):
        self.execute_test(3, [1,2,3])

    def test_get_fibonacci_max_4(self):
        self.execute_test(4, [1,2,3])

    def test_get_fibonacci_max_5(self):
        self.execute_test(5, [1,2,3,5])

    def test_get_fibonacci_max_6(self):
        self.execute_test(6, [1,2,3,5])

    def test_get_fibonacci_max_8(self):
        self.execute_test(8, [1,2,3,5,8])

    def test_get_fibonacci_max_89(self):
        self.execute_test(89, [1,2,3,5,8,13,21,34,55,89])
    
    def execute_test(self, max, expected_result):
        result = list(self.target.get_fibonacci(max))
        self.assertEqual(expected_result, result)
