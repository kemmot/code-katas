import functools as ft
import math


class LargestPrimeFactor:
    def execute(self, value):
        factors = FactorGenerator().get_factors(value)
        prime_factors = filter(PrimeChecker().is_prime, factors)
        return max(prime_factors)
    

class FactorGenerator:
    def get_factors(self, value):
        factors = []
        try:
            starting_factor = self.get_starting_factor(value)

            factors_to_try = []
            factors_to_try.append(starting_factor)

            while len(factors_to_try) > 0:
                factor_to_try = factors_to_try.pop()
                next_factor = int(value / factor_to_try)
                if not next_factor in factors:
                    factors_to_try.append(next_factor)
                    factors.append(next_factor)
                for next_factor in self.get_factors(factor_to_try):
                    if not next_factor in factors:
                        factors_to_try.append(next_factor)
                        factors.append(next_factor)
        except:
            # prime factor reached
            pass
        return factors

    def get_starting_factor(self, value):
        possible_factor = 2
        while possible_factor < value:
            if value % possible_factor == 0:
                return possible_factor
            else:
                possible_factor += 1
        raise Exception('No starting factor found')


class PrimeChecker:
    def is_prime(self, value):
        is_prime = True
        if value != 2:
            max_factor = math.ceil(math.sqrt(value))
            for divisor in range(2, max_factor + 1):
                if value % divisor == 0:
                    is_prime = False
        return is_prime
