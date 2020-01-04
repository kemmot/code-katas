import unittest

import p001_multiples_of_3_and_5 as implementation


class ImplementationTests(unittest.TestCase):
    def setUp(self):
        self.target = implementation.MultiplesOf3And5()
    
    def test_sum_of_multiples_below_4_is_3(self):
        self.execute_test(4, 3)
    
    def test_sum_of_multiples_below_6_is_8(self):
        self.execute_test(6, 8)
    
    def test_sum_of_multiples_below_7_is_14(self):
        self.execute_test(8, 14)

    def test_sum_of_multiples_below_10_is_23(self):
        self.execute_test(10, 23)

    def test_sum_of_multiples_below_11_is_33(self):
        self.execute_test(11, 33)

    def test_sum_of_multiples_below_13_is_45(self):
        self.execute_test(13, 45)

    def test_sum_of_multiples_below_1000(self):
        self.execute_test(1000, 266333)

    def execute_test(self, top, expected_result):
        result = self.target.execute(top)
        self.assertEqual(expected_result, result)