#path = 'day01_input_sample.txt'
path = 'day01_input01.txt'
list_a = []
list_b = []
with open(path, 'r') as file:
    for line in file.readlines():
        line = line.strip()
        parts = line.split()
        list_a.append(int(parts[0]))
        list_b.append(int(parts[1]))
if len(list_a) != len(list_b):
    raise Exception(f'Lists should be of same size, list a:{len(list_a)}, list b:{len(list_b)}')
#list_a_sorted = sorted(list_a)
#list_b_sorted = sorted(list_b)
total_similarity_score = 0
for index_a in range(0, len(list_a)):
    item_a = list_a[index_a]
    count = 0
    for index_b in range(0, len(list_b)):
        item_b = list_b[index_b]
        if item_a == item_b:
            count += 1
    similarity_score = item_a * count
    #if similarity_score < 0:
    #    distance *= -1
    #raise Exception(f'Distance cannot be less than zero, index:{index},item a:{item_a},item b:{item_b},distance:{distance}')
    total_similarity_score += similarity_score
print(f'total similarity score: {total_similarity_score}')
