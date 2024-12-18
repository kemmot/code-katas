#!/usr/bin/env python3

import re

#path = 'day03_input_sample.txt'
#path = 'day03_part02_input_sample.txt'
path = 'day03_input01.txt'

with open(path, 'r') as file:
    total = 0
    enabled = True
    for line in file.readlines():
        line = line.strip()

        pattern = '('
        pattern += 'mul\\((\\d{1,3}),(\\d{1,3})\\)'
        pattern += '|'
        pattern += 'do\\(\\)'
        pattern += '|'
        pattern += "don't\\(\\)"
        pattern += ')'
        result = re.findall(pattern, line)
        if result:
            for match in result:
                #print(match)
                if match[0].startswith('do('):
                    enabled = True
                elif match[0].startswith("don't("):
                    enabled = False
                elif enabled:
                    num1 = int(match[1])
                    num2 = int(match[2])
                    result = num1 * num2
                    total += result

    print(f'total: {total}')

