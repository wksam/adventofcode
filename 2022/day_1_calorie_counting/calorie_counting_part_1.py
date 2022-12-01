def read_file(path):
    return open(path).read().splitlines()

def most_calories(path):
    calories = read_file(path)
    most_calories = 0
    current_calorie = 0
    for calorie in calories:
        if calorie != '':
            current_calorie += int(calorie)
        else:
            if current_calorie > most_calories:
                most_calories = current_calorie
            current_calorie = 0
    return most_calories

path = '2022/day_1_calorie_counting/calories.txt'
print(most_calories(path))