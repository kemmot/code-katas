#!/usr/bin/env python3

import re

#path = 'day03_input_sample.txt'
path = 'day03_input01.txt'

with open(path, 'r') as file:
    total = 0
    for line in file.readlines():
        line = line.strip()

        pattern = 'mul\\((\\d{1,3}),(\\d{1,3})\\)'
        result = re.findall(pattern, line)
        if result:
            for match in result:
                num1 = int(match[0])
                num2 = int(match[1])
                result = num1 * num2
                total += result

    print(f'total: {total}')

