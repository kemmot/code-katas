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

    def execute_test(self, value, expected_result):
        result = self.target.execute(value)
        self.assertEqual(expected_result, result)


class PrimeGeneratorTests(unittest.TestCase):
    def test_first_primes(self):
        target = implementation.PrimeGenerator()
        primes = list(target.generate(20))
        self.assertEqual(2, primes[0])
        self.assertEqual(3, primes[1])
        self.assertEqual(5, primes[2])
        self.assertEqual(7, primes[3])
        self.assertEqual(11, primes[4])
        self.assertEqual(13, primes[5])
