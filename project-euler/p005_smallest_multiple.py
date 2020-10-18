class SmallestMultiple:
    def find_smallest_multiple(self, max_multiplier):
        possible_multiple = max_multiplier
        while True:
            if self.is_multiple_to_all(max_multiplier, possible_multiple):
                return possible_multiple
            else:
                possible_multiple += max_multiplier

    def is_multiple_to_all(self, max_multiplier, possible_multiple):
        for multiplier in range(1, max_multiplier + 1):
            if not self.is_multiple(multiplier, possible_multiple):
                return False
        return True
    
    def is_multiple(self, multiplier, possible_multiple):
        return possible_multiple % multiplier == 0

