import string

def read_file(path):
    return open(path).read()

def format_input(input, group_size):
    rucksacks = input.splitlines()
    groups = []
    for i in range(0, len(rucksacks), group_size):
        groups.append(rucksacks[i:i + group_size])
    return groups

def sum_of_the_priority_items(path):
    file = read_file(path)
    groups = format_input(file, 3)

    badges = []
    for group in groups:
        common_item = []
        for item in group[0]:
            if item in group[1] and item in group[2] and item not in common_item:
                common_item += item
        badges += common_item
    
    sum = 0
    priority_list = list(string.ascii_letters)
    for priority_item in badges:
        sum += priority_list.index(priority_item) + 1
    
    return sum

path = '2022/day_3_rucksack_reorganization/rucksack_items.txt'
print(sum_of_the_priority_items(path))