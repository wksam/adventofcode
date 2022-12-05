import string

def read_file(path):
    return open(path).read()

def format_input(input):
    return [[rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]] for rucksack in input.splitlines()]

def sum_of_the_priority_items(path):
    file = read_file(path)
    rucksacks = format_input(file)

    priority_items = []
    for rucksack in rucksacks:
        rucksack_priority_items = []
        for item in rucksack[0]:
            if item in rucksack[1]and item not in rucksack_priority_items:
                rucksack_priority_items.append(item)
        priority_items += rucksack_priority_items
    
    sum = 0
    priority_list = list(string.ascii_letters)
    for priority_item in priority_items:
        sum += priority_list.index(priority_item) + 1
    
    return sum

path = '2022/day_3_rucksack_reorganization/rucksack_items.txt'
print(sum_of_the_priority_items(path))