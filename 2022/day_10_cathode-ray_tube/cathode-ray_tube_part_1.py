def read_file(path):
    return open(path).read()

def format_input(input):
    return input.splitlines()

def sum_signal_strength(path):
    file = read_file(path)
    instructions = format_input(file)

    current_cycle = 0
    signal_strength = 0
    x = 1
    for instruction in instructions:
        if instruction == 'noop':
            current_cycle += 1
            signal_strength += calculate_signal_strength(current_cycle, x)
            continue
        else:
            v = int(instruction.split(' ')[1])
            for c in range(2):
                current_cycle += 1
                signal_strength += calculate_signal_strength(current_cycle, x)
                if(c > 0):
                    x += int(v)
    return signal_strength

def calculate_signal_strength(current_cycle, current_value):
    return current_cycle * current_value if (current_cycle - 20) % 40 == 0 else 0

path = '2022/day_10_cathode-ray_tube/instructions.txt'
print(sum_signal_strength(path))