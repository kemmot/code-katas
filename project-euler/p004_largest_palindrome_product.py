import math


class LargestPalindromeProduct:
    def find_largest_palindrome_product(self, digit_count):
        checker = PalindromeChecker()
        constituents = None
        max_palindrome = 0
        max_input_value = int(self.find_max_input_value(digit_count))
        for digit_1 in range(max_input_value, 0, -1):
            for digit_2 in range(max_input_value, 0, -1):
                product = digit_1 * digit_2
                if max_palindrome > 0 and product < max_palindrome:
                    break
                if checker.is_palindrome(product):
                    max_palindrome = product
                    constituents = [digit_1, digit_2]
        print('max: {}, {} x {}'.format(max_palindrome, constituents[0], constituents[1]))
        return max_palindrome

    def find_max_input_value(self, digit_count):
        return math.pow(10, digit_count) - 1


class PalindromeChecker:
    def is_palindrome(self, value):
        value_string = str(value)
        reversed_value_string = value_string[::-1]
        return value_string == reversed_value_string

