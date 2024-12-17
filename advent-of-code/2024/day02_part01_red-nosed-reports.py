#path = 'day02_input_sample.txt'
path = 'day02_input01.txt'

with open(path, 'r') as file:
    safe_count = 0
    for report in file.readlines():
        report = report.strip()
        levels = report.split(' ')
        last_level = None
        is_increasing = None
        is_report_safe = True

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

                #print(f'level:{level},increasing:{is_increasing},difference:{difference},is_level_safe:{is_level_safe},is_report_safe:{is_report_safe}')
            last_level = level

        if is_report_safe: safe_count += 1

print(f'Safe count: {safe_count}')
