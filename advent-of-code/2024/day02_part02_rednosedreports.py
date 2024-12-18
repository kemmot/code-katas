#!/usr/bin/env python3

#path = 'day02_input_sample.txt'
path = 'day02_input01.txt'

debug = False

def is_report_safe(levels):
    last_level = None
    is_increasing = None
    is_report_safe = True

    if debug: print(levels)

    for level in levels:
        level = int(level)
        if last_level != None:
            if is_increasing == None:
                if level > last_level:
                    is_increasing = True
                else:
                    # also caters for levels staying the same which will result in a difference of zero and therefore unsafe
                    is_increasing = False

            if is_increasing:
                difference = level - last_level
            else:
                difference = last_level - level

            is_level_safe = difference >= 1 and difference <= 3
            if not is_level_safe:
                is_report_safe = False

            if debug: print(f'\tlevel:{level},increasing:{is_increasing},difference:{difference},is_level_safe:{is_level_safe},is_report_safe:{is_report_safe}')

        last_level = level

    if debug: print(f'\tis report safe: {is_report_safe}')
    return is_report_safe

def is_report_safe_with_dampener(levels):
    report_is_safe = is_report_safe(levels)
    if report_is_safe: return report_is_safe

    for level_index in range(0, len(levels)):
        dampener_levels = levels.copy()
        del dampener_levels[level_index]
        report_is_safe = is_report_safe(dampener_levels)
        if report_is_safe: return report_is_safe

    return False

if __name__ == '__main__':
    debug = True
    with open(path, 'r') as file:
        safe_count = 0
        for report in file.readlines():
            report = report.strip()
            levels = report.split(' ')
            report_is_safe = is_report_safe_with_dampener(levels)
            if report_is_safe: safe_count += 1

    print(f'Safe count: {safe_count}')

