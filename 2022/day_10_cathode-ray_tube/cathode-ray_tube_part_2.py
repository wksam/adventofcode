import math

def read_file(path):
    return open(path).read()

def format_input(input):
    return input.splitlines()

def draw(path):
    file = read_file(path)
    instructions = format_input(file)

    current_cycle = 0
    crt = [['#' for _ in range(40)] for _ in range(6)]
    sprite = ['#'] * 3 + ['.'] * 37
    
    for instruction in instructions:
        if instruction == 'noop':
            crt[math.floor(current_cycle / 40)][current_cycle % 40] = sprite[current_cycle % 40]
            current_cycle += 1
            continue
        else:
            v = int(instruction.split(' ')[1])
            for c in range(2):
                crt[math.floor(current_cycle / 40)][current_cycle % 40] = sprite[current_cycle % 40]
                current_cycle += 1
                if(c > 0):
                    sprite = move_sprite(sprite, v)
    return crt

def move_sprite(sprite, value):
    return sprite[-value:] + sprite[:-value]

def ctr_print(crt):
    for pixel in crt:
        print(''.join(pixel))

path = '2022/day_10_cathode-ray_tube/instructions.txt'
ctr_print(draw(path))