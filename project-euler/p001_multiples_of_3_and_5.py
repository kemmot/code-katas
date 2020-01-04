class MultiplesOf3And5:
    def execute(self, top):
        result = 0
        for multiple in [3, 5]:
            result += sum(self.get_multiples(multiple, top))      
        return result
    
    def get_multiples(self, multiple, top):
        value = 0
        while value < top:
            yield value
            value += multiple