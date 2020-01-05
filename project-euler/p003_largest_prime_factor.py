import functools as ft


class LargestPrimeFactor:
    def execute(self, value):
        is_factor = ft.partial(self.is_factor, value=value)
        primes = PrimeGenerator().generate(int(value / 2))
        factors = filter(is_factor, primes)
        return max(factors)

    def is_factor(self, possible_factor, value):
        return value % possible_factor == 0


class PrimeGenerator:
    def generate(self, max):
        current_primes = []
        for value in range(2, max + 1):
            if self.is_prime(value, current_primes):
                current_primes.append(value)
                yield value
    
    def is_prime(self, value, current_primes):
        if value == 1:
            is_prime = False
        else:
            is_prime = True
            for prime in current_primes:
                if value % prime == 0:
                    is_prime = False
                    break
        return is_prime