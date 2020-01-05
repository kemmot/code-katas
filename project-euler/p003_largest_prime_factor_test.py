import unittest

import p003_largest_prime_factor as implementation


class ImplementationTests(unittest.TestCase):
    def setUp(self):
        self.target = implementation.LargestPrimeFactor()
    
    def test_largest_prime_factor_of_4_is_2(self):
        self.execute_test(4, 2)

    def test_largest_prime_factor_of_6_is_3(self):
        self.execute_test(6, 3)

    def test_largest_prime_factor_of_8_is_2(self):
        self.execute_test(8, 2)

    def test_largest_prime_factor_of_9_is_3(self):
        self.execute_test(9, 3)

    def test_largest_prime_factor_of_10_is_5(self):
        self.execute_test(10, 5)

    def test_largest_prime_factor_of_21_is_7(self):
        self.execute_test(21, 7)

    def test_largest_prime_factor_of_13195_is_29(self):
        self.execute_test(13195, 29)
    
    def test_largest_prime_factor_of_600851475143_is_29(self):
        self.execute_test(600851475143, 6857)    

    def execute_test(self, value, expected_result):
        result = self.target.execute(value)
        self.assertEqual(expected_result, result)


class FactorGeneratorTests(unittest.TestCase):
    def test_factors_of_6(self):
        factors = implementation.FactorGenerator().get_factors(6)
        factors.sort()
        self.assertEqual(2, len(factors))
        self.assertEqual(2, factors[0])
        self.assertEqual(3, factors[1])

    def test_factors_of_12(self):
        factors = implementation.FactorGenerator().get_factors(12)
        factors.sort()
        self.assertEqual(4, len(factors))
        self.assertEqual(2, factors[0])
        self.assertEqual(3, factors[1])
        self.assertEqual(4, factors[2])
        self.assertEqual(6, factors[3])

    def test_factors_of_20(self):
        factors = implementation.FactorGenerator().get_factors(20)
        factors.sort()
        self.assertEqual(4, len(factors))
        self.assertEqual(2, factors[0])
        self.assertEqual(4, factors[1])
        self.assertEqual(5, factors[2])
        self.assertEqual(10, factors[3])


class PrimeCheckerTests(unittest.TestCase):
    def test_is_2_prime(self):
        self.assertTrue(implementation.PrimeChecker().is_prime(2))

    def test_is_3_prime(self):
        self.assertTrue(implementation.PrimeChecker().is_prime(3))

    def test_is_4_prime(self):
        self.assertFalse(implementation.PrimeChecker().is_prime(4))

    def test_is_5_prime(self):
        self.assertTrue(implementation.PrimeChecker().is_prime(5))

    def test_is_6_prime(self):
        self.assertFalse(implementation.PrimeChecker().is_prime(6))

    def test_is_7_prime(self):
        self.assertTrue(implementation.PrimeChecker().is_prime(7))

    def test_is_10_prime(self):
        self.assertFalse(implementation.PrimeChecker().is_prime(10))

    def test_is_17_prime(self):
        self.assertTrue(implementation.PrimeChecker().is_prime(17))

    def test_is_7918_prime(self):
        self.assertFalse(implementation.PrimeChecker().is_prime(7918))

    def test_is_7919_prime(self):
        self.assertTrue(implementation.PrimeChecker().is_prime(7919))

    def test_is_7920_prime(self):
        self.assertFalse(implementation.PrimeChecker().is_prime(7920))
