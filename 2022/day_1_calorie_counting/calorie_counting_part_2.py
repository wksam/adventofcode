def read_file(path):
    return open(path).read()

def format_input(input):
    return [[int(calorie) for calorie in elf.split('\n')] for elf in input.split('\n\n')]

def calculate_calories(elves):
    calories = []
    for elf in elves:
        sum = 0
        for calorie in elf:
            sum += calorie
        calories.append(sum)
    return calories

def most_calories(path):
    file = read_file(path)
    elves = format_input(file)
    calories = calculate_calories(elves)
    calories.sort()
    sum = 0
    for _ in range(3):
        sum += calories.pop()
    return sum

path = '2022/day_1_calorie_counting/calories.txt'
print(most_calories(path))