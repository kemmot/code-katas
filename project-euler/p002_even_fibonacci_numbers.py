class EvenFibonacciNumbers:
    def execute(self, max):
        fibonacci_generator = FibonacciGenerator()

        result = 0
        for fibonacci_number in fibonacci_generator.get_fibonacci(max):
            if fibonacci_number % 2 == 0:
                result += fibonacci_number
        
        return result


class FibonacciGenerator:
    def get_fibonacci(self, max):
        value = 0
        previous_value = 0
        previous_previous_value = 0
        while value <= max:
            previous_previous_value = previous_value
            previous_value = value

            if value == 0:
                value = 1
            elif value == 1:
                value = 2
            else:
                value = previous_value + previous_previous_value
            
            if value <= max:
                yield value